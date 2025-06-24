from PySide6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt


class ExportFormatDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Выбор формата экспорта")
        self.setFixedSize(320, 280)  
        self.setStyleSheet("""
            QDialog {
                background-color: #F5F6F5;
                font: 10pt "Segoe UI";
                color: #333333;
            }
            QPushButton {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4A90E2, stop:1 #357ABD);
                color: #FFFFFF;
                border: none;
                border-radius: 6px;
                padding: 12px;  /* Увеличил padding */
                margin: 6px;    /* Добавил margin */
                font: bold 10pt "Segoe UI";
                min-width: 100px;
                min-height: 36px;
            }
            QPushButton:hover {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #357ABD, stop:1 #2D5D9F);
            }
            QPushButton:pressed {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #2D5D9F, stop:1 #254C80);
            }
            QPushButton#cancelButton {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #E24A4A, stop:1 #BD3535);
            }
            QPushButton#cancelButton:hover {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #BD3535, stop:1 #9F2D2D);
            }
            QPushButton#cancelButton:pressed {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #9F2D2D, stop:1 #802525);
            }
            QPushButton:disabled {
                background-color: #CCCCCC;
                color: #666666;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24) 
        layout.setSpacing(16)  

        self.excel_button = QPushButton("Экспорт в Excel (XLSX)")
        self.pdf_button = QPushButton("Экспорт в PDF")
        self.cancel_button = QPushButton("Отмена")
        self.cancel_button.setObjectName("cancelButton")
        self.cancel_button.setCursor(Qt.PointingHandCursor)

        for btn in (self.excel_button, self.pdf_button, self.cancel_button):
            btn.setMinimumHeight(36)
            btn.setCursor(Qt.PointingHandCursor)

        self.excel_button.clicked.connect(lambda: self.select_format("xlsx"))
        self.pdf_button.clicked.connect(lambda: self.select_format("pdf"))
        self.cancel_button.clicked.connect(self.reject)

        layout.addWidget(self.excel_button)
        layout.addWidget(self.pdf_button)
        layout.addWidget(self.cancel_button)
        layout.addStretch()

    def select_format(self, format_type):
        self.selected_format = format_type
        self.accept()