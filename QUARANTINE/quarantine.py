from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QMessageBox,
)


class Quarantine(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("QUARANTINE")
        title.setStyleSheet(
            "font-size: 28px; font-weight: bold;"
        )

        subtitle = QLabel(
            "Manage files isolated from the system."
        )

        self.files = QListWidget()
        self.files.addItem("No quarantined files")

        buttons = QHBoxLayout()

        restore_btn = QPushButton("Restore")
        delete_btn = QPushButton("Delete Permanently")
        refresh_btn = QPushButton("Refresh")

        restore_btn.clicked.connect(self.restore_file)
        delete_btn.clicked.connect(self.delete_file)
        refresh_btn.clicked.connect(self.refresh)

        buttons.addWidget(restore_btn)
        buttons.addWidget(delete_btn)
        buttons.addWidget(refresh_btn)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(self.files)
        layout.addLayout(buttons)

    def restore_file(self):
        QMessageBox.information(
            self,
            "Restore",
            "Restore action will be connected to the backend later."
        )

    def delete_file(self):
        QMessageBox.information(
            self,
            "Delete",
            "Permanent deletion will be connected to the backend later."
        )

    def refresh(self):
        QMessageBox.information(
            self,
            "Refresh",
            "Quarantine list refreshed."
        )
