from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QPushButton,
    QMessageBox,
)


class ThreatDatabase(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("THREAT DATABASE")
        title.setStyleSheet(
            "font-size: 28px; font-weight: bold;"
        )

        subtitle = QLabel(
            "Browse and search known malware signatures."
        )

        self.search = QLineEdit()
        self.search.setPlaceholderText(
            "Search threat name, hash, or signature..."
        )

        self.threats = QListWidget()

        self.threats.addItem("No threat records available")
        self.threats.addItem("Database will be connected later")
        self.threats.addItem("Malware signatures")
        self.threats.addItem("YARA detection rules")
        self.threats.addItem("File hash signatures")

        buttons = QHBoxLayout()

        search_btn = QPushButton("Search")
        refresh_btn = QPushButton("Refresh")

        search_btn.clicked.connect(self.search_threat)
        refresh_btn.clicked.connect(self.refresh)

        buttons.addWidget(search_btn)
        buttons.addWidget(refresh_btn)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(self.search)
        layout.addWidget(self.threats)
        layout.addLayout(buttons)

    def search_threat(self):
        query = self.search.text().strip()

        if query:
            QMessageBox.information(
                self,
                "Threat Search",
                f"Searching for: {query}\n\n"
                "Database connection will be added later."
            )
        else:
            QMessageBox.warning(
                self,
                "Search",
                "Enter a threat name, hash, or signature."
            )

    def refresh(self):
        QMessageBox.information(
            self,
            "Refresh",
            "Threat database refreshed."
        )
