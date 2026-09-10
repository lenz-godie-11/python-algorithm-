from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QMessageBox,
)


class ScanHistory(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("SCAN HISTORY")
        title.setStyleSheet(
            "font-size: 28px; font-weight: bold;"
        )

        subtitle = QLabel(
            "View previous antivirus scan activities."
        )

        self.history = QTableWidget()
        self.history.setColumnCount(4)
        self.history.setHorizontalHeaderLabels(
            ["Date", "Scan Type", "Files Scanned", "Result"]
        )

        self.history.setRowCount(3)

        data = [
            ["Today", "Quick Scan", "0", "No threats"],
            ["Yesterday", "File Scan", "0", "No threats"],
            ["Previous", "Full Scan", "0", "No threats"],
        ]

        for row, values in enumerate(data):
            for column, value in enumerate(values):
                self.history.setItem(
                    row,
                    column,
                    QTableWidgetItem(value)
                )

        self.history.horizontalHeader().setStretchLastSection(True)

        buttons = QHBoxLayout()

        refresh_btn = QPushButton("Refresh")
        clear_btn = QPushButton("Clear History")

        refresh_btn.clicked.connect(self.refresh)
        clear_btn.clicked.connect(self.clear_history)

        buttons.addWidget(refresh_btn)
        buttons.addWidget(clear_btn)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(self.history)
        layout.addLayout(buttons)

    def refresh(self):
        QMessageBox.information(
            self,
            "Refresh",
            "Scan history refreshed."
        )

    def clear_history(self):
        self.history.setRowCount(0)
