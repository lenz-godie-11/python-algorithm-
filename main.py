import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QStackedWidget,
    QFileDialog,
)

from DASHBOARD.dashboard import Dashboard
from PROGRESS.progress import Progress
from SCANRESULT.scanresult import ScanResult


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SENTINEL - Homegrown Antivirus")
        self.resize(1200, 750)

        self.setup_ui()

    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout(central)

        sidebar = QVBoxLayout()

        dashboard_btn = QPushButton("Dashboard")
        scan_btn = QPushButton("Scan")
        progress_btn = QPushButton("Progress")
        results_btn = QPushButton("Scan Results")

        sidebar.addWidget(dashboard_btn)
        sidebar.addWidget(scan_btn)
        sidebar.addWidget(progress_btn)
        sidebar.addWidget(results_btn)
        sidebar.addStretch()

        self.pages = QStackedWidget()

        self.dashboard = Dashboard(self.start_scan)
        self.scan_page = self.create_scan_page()
        self.progress = Progress(self.cancel_scan)
        self.results = ScanResult()

        self.pages.addWidget(self.dashboard)
        self.pages.addWidget(self.scan_page)
        self.pages.addWidget(self.progress)
        self.pages.addWidget(self.results)

        dashboard_btn.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.dashboard)
        )

        scan_btn.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.scan_page)
        )

        progress_btn.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.progress)
        )

        results_btn.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.results)
        )

        main_layout.addLayout(sidebar)
        main_layout.addWidget(self.pages)

    def create_scan_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        file_btn = QPushButton("Select File")
        folder_btn = QPushButton("Select Folder")
        quick_btn = QPushButton("Quick Scan")
        full_btn = QPushButton("Full Scan")

        file_btn.clicked.connect(self.select_file)
        folder_btn.clicked.connect(self.select_folder)

        quick_btn.clicked.connect(
            lambda: self.start_scan("quick")
        )

        full_btn.clicked.connect(
            lambda: self.start_scan("full")
        )

        layout.addWidget(file_btn)
        layout.addWidget(folder_btn)
        layout.addWidget(quick_btn)
        layout.addWidget(full_btn)
        layout.addStretch()

        return page

    def select_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Select File"
        )

        if path:
            self.start_scan("file", path)

    def select_folder(self):
        path = QFileDialog.getExistingDirectory(
            self,
            "Select Folder"
        )

        if path:
            self.start_scan("folder", path)

    def start_scan(self, scan_type, path=None):
        self.pages.setCurrentWidget(self.progress)

        self.progress.stage.setText(
            f"{scan_type.upper()} SCAN READY"
        )

        if path:
            self.progress.current_file.setText(
                f"Selected: {path}"
            )
        else:
            self.progress.current_file.setText(
                "Waiting for scanning engine..."
            )

        self.progress.counter.setText(
            "Files scanned: 0"
        )

        self.progress.bar.setValue(0)

    def cancel_scan(self):
        self.pages.setCurrentWidget(self.scan_page)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()