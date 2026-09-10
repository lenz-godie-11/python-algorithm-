from PySide6.QtCore import QObject, Signal
from pathlib import Path
import hashlib
import os
import re


class Scanner(QObject):
    file_found = Signal(str, int)
    finished = Signal(list)

    def __init__(self, target):
        super().__init__()
        self.target = Path(target)
        self.cancelled = False

    def cancel(self):
        self.cancelled = True

    def collect_files(self):
        if self.target.is_file():
            return [self.target]

        if self.target.is_dir():
            return [
                p for p in self.target.rglob("*")
                if p.is_file()
            ]

        return []

    def sha256(self, path):
        h = hashlib.sha256()

        with open(path, "rb") as f:
            while chunk := f.read(1024 * 1024):
                h.update(chunk)

        return h.hexdigest()

    def analyze(self, path):
        reasons = []
        suspicious_score = 0

        name = path.name.lower()

        dangerous_extensions = {
            ".exe", ".dll", ".scr", ".bat", ".cmd",
            ".ps1", ".vbs", ".js", ".msi", ".com"
        }

        if path.suffix.lower() in dangerous_extensions:
            suspicious_score += 20
            reasons.append("Executable or script file")

        try:
            data = path.read_bytes()[:5 * 1024 * 1024]

            strings = re.findall(
                rb"[ -~]{6,}",
                data
            )

            text = b" ".join(strings).lower()

            indicators = [
                b"powershell",
                b"cmd.exe",
                b"wscript",
                b"cscript",
                b"downloadstring",
                b"invoke-expression",
                b"rundll32",
                b"regsvr32",
                b"encodedcommand"
            ]

            for indicator in indicators:
                if indicator in text:
                    suspicious_score += 15
                    reasons.append(
                        f"Suspicious indicator: {indicator.decode(errors='ignore')}"
                    )

        except (PermissionError, OSError):
            reasons.append("File could not be fully read")

        if suspicious_score >= 50:
            status = "MALICIOUS"
        elif suspicious_score >= 20:
            status = "SUSPICIOUS"
        else:
            status = "SAFE"

        return {
            "file": str(path),
            "name": path.name,
            "size": path.stat().st_size,
            "sha256": self.sha256(path),
            "status": status,
            "risk_score": min(suspicious_score, 100),
            "reasons": reasons
        }

    def run(self):
        files = self.collect_files()
        results = []

        for index, path in enumerate(files, start=1):
            if self.cancelled:
                break

            try:
                result = self.analyze(path)
                results.append(result)
                self.file_found.emit(str(path), index)
            except (PermissionError, OSError):
                continue

        self.finished.emit(results)
