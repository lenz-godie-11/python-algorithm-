from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from pathlib import Path
import json


class Dashboard(QWidget):
    def __init__(self, start_scan):
        super().__init__()
        self.start_scan = start_scan

        layout = QVBoxLayout(self)

        title = QLabel("TANZANITE SENTINEL")
        title.setStyleSheet("font-size: 28px; font-weight: bold;")

        self.status = QLabel("● PROTECTION ACTIVE")
        self.status.setStyleSheet("color: green; font-size: 18px;")

        self.files = QLabel()
        self.threats = QLabel()
        self.suspicious = QLabel()

        layout.addWidget(title)
        layout.addWidget(self.status)
        layout.addWidget(self.files)
        layout.addWidget(self.threats)
        layout.addWidget(self.suspicious)

        buttons = QHBoxLayout()

        quick = QPushButton("Quick Scan")
        quick.clicked.connect(lambda: self.start_scan("quick"))

        file_scan = QPushButton("Scan File")
        file_scan.clicked.connect(lambda: self.start_scan("file"))

        folder_scan = QPushButton("Scan Folder")
        folder_scan.clicked.connect(lambda: self.start_scan("folder"))

        buttons.addWidget(quick)
        buttons.addWidget(file_scan)
        buttons.addWidget(folder_scan)

        layout.addLayout(buttons)
        self.refresh()

    def refresh(self):
        history = Path("scan_history.json")

        scanned = threats = suspicious = 0

        if history.exists():
            try:
                data = json.loads(history.read_text())
                for scan in data:
                    scanned += scan.get("files_scanned", 0)
                    threats += scan.get("malicious", 0)
                    suspicious += scan.get("suspicious", 0)
            except Exception:
                pass

        self.files.setText(f"Files Scanned: {scanned}")
        self.threats.setText(f"Threats Detected: {threats}")
        self.suspicious.setText(f"Suspicious Files: {suspicious}")
