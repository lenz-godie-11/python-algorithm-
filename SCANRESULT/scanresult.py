from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton


class ScanResult(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.summary = QLabel("Scan Results")
        self.summary.setStyleSheet("font-size: 24px; font-weight: bold;")

        self.list = QListWidget()

        self.details = QLabel("Select a file to view details.")
        self.details.setWordWrap(True)

        self.list.currentRowChanged.connect(self.show_details)

        layout.addWidget(self.summary)
        layout.addWidget(self.list)
        layout.addWidget(self.details)

        self.results = []

    def display_results(self, results):
        self.results = results
        self.list.clear()

        malicious = sum(r["status"] == "MALICIOUS" for r in results)
        suspicious = sum(r["status"] == "SUSPICIOUS" for r in results)

        self.summary.setText(
            f"Scan Complete — {len(results)} files | "
            f"{malicious} malicious | {suspicious} suspicious"
        )

        for result in results:
            self.list.addItem(
                f"[{result['status']}] {result['name']} "
                f"(Risk: {result['risk_score']})"
            )

    def show_details(self, index):
        if index < 0 or index >= len(self.results):
            return

        r = self.results[index]

        reasons = "\n".join(r["reasons"]) or "No suspicious indicators found."

        self.details.setText(
            f"File: {r['name']}\n"
            f"Path: {r['file']}\n"
            f"Size: {r['size']} bytes\n"
            f"SHA-256: {r['sha256']}\n"
            f"Status: {r['status']}\n"
            f"Risk Score: {r['risk_score']}/100\n\n"
            f"Detection Reasons:\n{reasons}"
        )
