import os
import sys
import logging
from PySide6.QtWidgets import QApplication, QSplashScreen
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt, QTimer

from ui.main_window import MainWindow
from utils.path_utils import resource_path


if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    level=logging.DEBUG,
    filename=os.path.join("logs", "app.log"),
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        path = resource_path('res/icons/icon-512x512.png')
        splash_pix = QPixmap(path) 
        splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
        splash.setFont(QFont("Segoe UI", 10))
        splash.showMessage("Загрузка, пожалуйста подождите...", Qt.AlignBottom | Qt.AlignHCenter, Qt.white)
        splash.show()
        app.processEvents()

        window = MainWindow()

        QTimer.singleShot(500, lambda: (
            window.showMaximized(),
            splash.finish(window)
        ))

        sys.exit(app.exec())

    except Exception as e:
        logger.error(f"Ошибка запуска приложения: {str(e)}")
        raise
