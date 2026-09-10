from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QCheckBox,
    QComboBox,
    QPushButton,
    QMessageBox,
    QGroupBox,
)


class Settings(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("SETTINGS")
        title.setStyleSheet(
            "font-size: 28px; font-weight: bold;"
        )

        subtitle = QLabel(
            "Configure SENTINEL antivirus preferences."
        )

        protection_group = QGroupBox("Protection")

        protection_layout = QVBoxLayout(protection_group)

        real_time = QCheckBox("Enable Real-Time Protection")
        real_time.setChecked(True)

        startup = QCheckBox("Start SENTINEL with system")
        startup.setChecked(True)

        notifications = QCheckBox("Enable Security Notifications")
        notifications.setChecked(True)

        protection_layout.addWidget(real_time)
        protection_layout.addWidget(startup)
        protection_layout.addWidget(notifications)

        scan_group = QGroupBox("Scanning")

        scan_layout = QVBoxLayout(scan_group)

        label = QLabel("Default Scan Type:")

        scan_type = QComboBox()
        scan_type.addItems([
            "Quick Scan",
            "Full Scan",
            "File Scan",
            "Folder Scan",
        ])

        scan_layout.addWidget(label)
        scan_layout.addWidget(scan_type)

        buttons = QHBoxLayout()

        save_btn = QPushButton("Save Settings")
        reset_btn = QPushButton("Reset")

        save_btn.clicked.connect(self.save_settings)
        reset_btn.clicked.connect(self.reset_settings)

        buttons.addWidget(save_btn)
        buttons.addWidget(reset_btn)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(protection_group)
        layout.addWidget(scan_group)
        layout.addLayout(buttons)
        layout.addStretch()

    def save_settings(self):
        QMessageBox.information(
            self,
            "Settings",
            "Settings saved successfully."
        )

    def reset_settings(self):
        QMessageBox.information(
            self,
            "Settings",
            "Settings restored to default."
        )
