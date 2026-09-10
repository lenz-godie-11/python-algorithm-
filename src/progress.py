from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar, QPushButton


class Progress(QWidget):
    def __init__(self, cancel_scan):
        super().__init__()

        self.cancel_scan = cancel_scan

        layout = QVBoxLayout(self)

        self.stage = QLabel("Preparing scan...")
        self.current_file = QLabel("Current file: -")
        self.counter = QLabel("Files scanned: 0")

        self.bar = QProgressBar()
        self.bar.setRange(0, 100)

        cancel = QPushButton("Cancel Scan")
        cancel.clicked.connect(self.cancel_scan)

        layout.addWidget(self.stage)
        layout.addWidget(self.current_file)
        layout.addWidget(self.counter)
        layout.addWidget(self.bar)
        layout.addWidget(cancel)

    def update_progress(self, current_file, number, total):
        self.current_file.setText(f"Current file: {current_file}")
        self.counter.setText(f"Files scanned: {number}")

        if total:
            self.bar.setValue(int((number / total) * 100))

        self.stage.setText("Analyzing file...")
