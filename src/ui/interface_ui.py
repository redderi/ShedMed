# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTableView, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1377, 900)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"\n"
"    QMainWindow {\n"
"        background-color: #F5F6F5;\n"
"        font: 10pt \"Segoe UI\";\n"
"        color: #333333;\n"
"    }\n"
"    QWidget {\n"
"        background-color: #FFFFFF;\n"
"        border-radius: 8px;\n"
"    }\n"
"   ")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, -1, -1, -1)
        self.main_button = QToolButton(self.centralWidget)
        self.main_button.setObjectName(u"main_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_button.sizePolicy().hasHeightForWidth())
        self.main_button.setSizePolicy(sizePolicy1)
        self.main_button.setMinimumSize(QSize(110, 80))
        self.main_button.setMaximumSize(QSize(110, 80))
        self.main_button.setStyleSheet(u"\n"
"            QToolButton {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #F0F0F0, stop:1 #E0E0E0);\n"
"                border: 1px solid #B0B0B0;\n"
"                border-radius: 6px;\n"
"                padding: 8px;\n"
"                margin: 4px;\n"
"                color: #333333;\n"
"                font: bold 10pt \"Segoe UI\";\n"
"                text-align: center;\n"
"            }\n"
"            QToolButton:hover {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #E0E0E0, stop:1 #D0D0D0);\n"
"                border: 1px solid #909090;\n"
"            }\n"
"            QToolButton:pressed {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #D0D0D0, stop:1 #C0C0C0);\n"
"                border: 1px solid #707070;\n"
"            }\n"
"            QToolButton:checked {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y"
                        "2:1, stop:0 #A0C0FF, stop:1 #80A0FF);\n"
"                border: 1px solid #6090FF;\n"
"            }\n"
"            QToolButton::icon {\n"
"                padding-bottom: 4px;\n"
"            }\n"
"         ")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoHome))
        self.main_button.setIcon(icon)
        self.main_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.main_button)

        self.event_button = QToolButton(self.centralWidget)
        self.event_button.setObjectName(u"event_button")
        sizePolicy1.setHeightForWidth(self.event_button.sizePolicy().hasHeightForWidth())
        self.event_button.setSizePolicy(sizePolicy1)
        self.event_button.setMinimumSize(QSize(110, 80))
        self.event_button.setMaximumSize(QSize(110, 80))
        self.event_button.setStyleSheet(u"\n"
"            QToolButton {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #F0F0F0, stop:1 #E0E0E0);\n"
"                border: 1px solid #B0B0B0;\n"
"                border-radius: 6px;\n"
"                padding: 8px;\n"
"                margin: 4px;\n"
"                color: #333333;\n"
"                font: bold 10pt \"Segoe UI\";\n"
"                text-align: center;\n"
"            }\n"
"            QToolButton:hover {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #E0E0E0, stop:1 #D0D0D0);\n"
"                border: 1px solid #909090;\n"
"            }\n"
"            QToolButton:pressed {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #D0D0D0, stop:1 #C0C0C0);\n"
"                border: 1px solid #707070;\n"
"            }\n"
"            QToolButton:checked {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y"
                        "2:1, stop:0 #A0C0FF, stop:1 #80A0FF);\n"
"                border: 1px solid #6090FF;\n"
"            }\n"
"            QToolButton::icon {\n"
"                padding-bottom: 4px;\n"
"            }\n"
"         ")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpenRecent))
        self.event_button.setIcon(icon1)
        self.event_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.event_button)

        self.backups_button = QToolButton(self.centralWidget)
        self.backups_button.setObjectName(u"backups_button")
        sizePolicy1.setHeightForWidth(self.backups_button.sizePolicy().hasHeightForWidth())
        self.backups_button.setSizePolicy(sizePolicy1)
        self.backups_button.setMinimumSize(QSize(110, 80))
        self.backups_button.setMaximumSize(QSize(110, 80))
        self.backups_button.setStyleSheet(u"\n"
"            QToolButton {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #F0F0F0, stop:1 #E0E0E0);\n"
"                border: 1px solid #B0B0B0;\n"
"                border-radius: 6px;\n"
"                padding: 8px;\n"
"                margin: 4px;\n"
"                color: #333333;\n"
"                font: bold 10pt \"Segoe UI\";\n"
"                text-align: center;\n"
"            }\n"
"            QToolButton:hover {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #E0E0E0, stop:1 #D0D0D0);\n"
"                border: 1px solid #909090;\n"
"            }\n"
"            QToolButton:pressed {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #D0D0D0, stop:1 #C0C0C0);\n"
"                border: 1px solid #707070;\n"
"            }\n"
"            QToolButton:checked {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y"
                        "2:1, stop:0 #A0C0FF, stop:1 #80A0FF);\n"
"                border: 1px solid #6090FF;\n"
"            }\n"
"            QToolButton::icon {\n"
"                padding-bottom: 4px;\n"
"            }\n"
"         ")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditCopy))
        self.backups_button.setIcon(icon2)
        self.backups_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.backups_button)

        self.export_button = QToolButton(self.centralWidget)
        self.export_button.setObjectName(u"export_button")
        sizePolicy1.setHeightForWidth(self.export_button.sizePolicy().hasHeightForWidth())
        self.export_button.setSizePolicy(sizePolicy1)
        self.export_button.setMinimumSize(QSize(110, 80))
        self.export_button.setMaximumSize(QSize(110, 80))
        self.export_button.setStyleSheet(u"\n"
"            QToolButton {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #F0F0F0, stop:1 #E0E0E0);\n"
"                border: 1px solid #B0B0B0;\n"
"                border-radius: 6px;\n"
"                padding: 8px;\n"
"                margin: 4px;\n"
"                color: #333333;\n"
"                font: bold 10pt \"Segoe UI\";\n"
"                text-align: center;\n"
"            }\n"
"            QToolButton:hover {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #E0E0E0, stop:1 #D0D0D0);\n"
"                border: 1px solid #909090;\n"
"            }\n"
"            QToolButton:pressed {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #D0D0D0, stop:1 #C0C0C0);\n"
"                border: 1px solid #707070;\n"
"            }\n"
"            QToolButton:checked {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y"
                        "2:1, stop:0 #A0C0FF, stop:1 #80A0FF);\n"
"                border: 1px solid #6090FF;\n"
"            }\n"
"            QToolButton::icon {\n"
"                padding-bottom: 4px;\n"
"            }\n"
"         ")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSend))
        self.export_button.setIcon(icon3)
        self.export_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.export_button)

        self.import_button = QToolButton(self.centralWidget)
        self.import_button.setObjectName(u"import_button")
        sizePolicy1.setHeightForWidth(self.import_button.sizePolicy().hasHeightForWidth())
        self.import_button.setSizePolicy(sizePolicy1)
        self.import_button.setMinimumSize(QSize(110, 80))
        self.import_button.setMaximumSize(QSize(110, 80))
        self.import_button.setStyleSheet(u"\n"
"            QToolButton {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #F0F0F0, stop:1 #E0E0E0);\n"
"                border: 1px solid #B0B0B0;\n"
"                border-radius: 6px;\n"
"                padding: 8px;\n"
"                margin: 4px;\n"
"                color: #333333;\n"
"                font: bold 10pt \"Segoe UI\";\n"
"                text-align: center;\n"
"            }\n"
"            QToolButton:hover {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #E0E0E0, stop:1 #D0D0D0);\n"
"                border: 1px solid #909090;\n"
"            }\n"
"            QToolButton:pressed {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #D0D0D0, stop:1 #C0C0C0);\n"
"                border: 1px solid #707070;\n"
"            }\n"
"            QToolButton:checked {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y"
                        "2:1, stop:0 #A0C0FF, stop:1 #80A0FF);\n"
"                border: 1px solid #6090FF;\n"
"            }\n"
"            QToolButton::icon {\n"
"                padding-bottom: 4px;\n"
"            }\n"
"         ")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailSend))
        self.import_button.setIcon(icon4)
        self.import_button.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.import_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.import_button.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout.addWidget(self.import_button)

        self.guide_button = QToolButton(self.centralWidget)
        self.guide_button.setObjectName(u"guide_button")
        self.guide_button.setMinimumSize(QSize(110, 80))
        self.guide_button.setMaximumSize(QSize(110, 80))
        self.guide_button.setStyleSheet(u"\n"
"            QToolButton {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #F0F0F0, stop:1 #E0E0E0);\n"
"                border: 1px solid #B0B0B0;\n"
"                border-radius: 6px;\n"
"                padding: 8px;\n"
"                margin: 4px;\n"
"                color: #333333;\n"
"                font: bold 10pt \"Segoe UI\";\n"
"                text-align: center;\n"
"            }\n"
"            QToolButton:hover {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #E0E0E0, stop:1 #D0D0D0);\n"
"                border: 1px solid #909090;\n"
"            }\n"
"            QToolButton:pressed {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #D0D0D0, stop:1 #C0C0C0);\n"
"                border: 1px solid #707070;\n"
"            }\n"
"            QToolButton:checked {\n"
"                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y"
                        "2:1, stop:0 #A0C0FF, stop:1 #80A0FF);\n"
"                border: 1px solid #6090FF;\n"
"            }\n"
"            QToolButton::icon {\n"
"                padding-bottom: 4px;\n"
"            }\n"
"         ")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentPageSetup))
        self.guide_button.setIcon(icon5)
        self.guide_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.guide_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.stackedWidget = QStackedWidget(self.centralWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.stackedWidget.setStyleSheet(u"\n"
"        QStackedWidget {\n"
"            background-color: #FFFFFF;\n"
"            border: 1px solid #D3D3D3;\n"
"            border-radius: 8px;\n"
"            padding-top: 8px;\n"
"        }\n"
"       ")
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        sizePolicy.setHeightForWidth(self.main_page.sizePolicy().hasHeightForWidth())
        self.main_page.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.main_page)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setSpacing(8)
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.create_button = QPushButton(self.main_page)
        self.create_button.setObjectName(u"create_button")
        self.create_button.setMinimumSize(QSize(120, 36))
        self.create_button.setStyleSheet(u"\n"
"                QPushButton {\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4A90E2, stop:1 #357ABD);\n"
"                    color: #FFFFFF;\n"
"                    border: none;\n"
"                    border-radius: 6px;\n"
"                    padding: 10px;\n"
"                    font: bold 10pt \"Segoe UI\";\n"
"                }\n"
"                QPushButton:hover {\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #357ABD, stop:1 #2D5D9F);\n"
"                }\n"
"                QPushButton:pressed {\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #2D5D9F, stop:1 #254C80);\n"
"                }\n"
"                QPushButton:disabled {\n"
"                    background-color: #CCCCCC;\n"
"                    color: #666666;\n"
"                }\n"
"             ")

        self.buttonLayout.addWidget(self.create_button)

        self.edit_button = QPushButton(self.main_page)
        self.edit_button.setObjectName(u"edit_button")
        self.edit_button.setMinimumSize(QSize(120, 36))
        self.edit_button.setStyleSheet(u"\n"
"                QPushButton {\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4A90E2, stop:1 #357ABD);\n"
"                    color: #FFFFFF;\n"
"                    border: none;\n"
"                    border-radius: 6px;\n"
"                    padding: 10px;\n"
"                    font: bold 10pt \"Segoe UI\";\n"
"                }\n"
"                QPushButton:hover {\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #357ABD, stop:1 #2D5D9F);\n"
"                }\n"
"                QPushButton:pressed {\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #2D5D9F, stop:1 #254C80);\n"
"                }\n"
"                QPushButton:disabled {\n"
"                    background-color: #CCCCCC;\n"
"                    color: #666666;\n"
"                }\n"
"             ")

        self.buttonLayout.addWidget(self.edit_button)

        self.delete_button = QPushButton(self.main_page)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setMinimumSize(QSize(120, 36))
        self.delete_button.setStyleSheet(u"\n"
"                QPushButton {\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #E24A4A, stop:1 #BD3535);\n"
"                    color: #FFFFFF;\n"
"                    border: none;\n"
"                    border-radius: 6px;\n"
"                    padding: 10px;\n"
"                    font: bold 10pt \"Segoe UI\";\n"
"                }\n"
"                QPushButton:hover {\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #BD3535, stop:1 #9F2D2D);\n"
"                }\n"
"                QPushButton:pressed {\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #9F2D2D, stop:1 #802525);\n"
"                }\n"
"                QPushButton:disabled {\n"
"                    background-color: #CCCCCC;\n"
"                    color: #666666;\n"
"                }\n"
"             ")

        self.buttonLayout.addWidget(self.delete_button)

        self.searchLabel = QLabel(self.main_page)
        self.searchLabel.setObjectName(u"searchLabel")
        self.searchLabel.setStyleSheet(u"\n"
"                QLabel {\n"
"                    color: #333333;\n"
"                    font: 10pt \"Segoe UI\";\n"
"                    padding: 8px;\n"
"                }\n"
"             ")

        self.buttonLayout.addWidget(self.searchLabel)

        self.searchLineEdit = QLineEdit(self.main_page)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setMinimumSize(QSize(200, 36))
        self.searchLineEdit.setStyleSheet(u"\n"
"                QLineEdit {\n"
"                    background-color: #FFFFFF;\n"
"                    border: 1px solid #B0B0B0;\n"
"                    border-radius: 6px;\n"
"                    padding: 8px;\n"
"                    color: #333333;\n"
"                    font: 10pt \"Segoe UI\";\n"
"                }\n"
"                QLineEdit:focus {\n"
"                    border: 1px solid #4A90E2;\n"
"                    background-color: #F9FAFB;\n"
"                }\n"
"                QLineEdit::placeholder {\n"
"                    color: #999999;\n"
"                }\n"
"             ")

        self.buttonLayout.addWidget(self.searchLineEdit)

        self.searchColumnComboBox = QComboBox(self.main_page)
        self.searchColumnComboBox.setObjectName(u"searchColumnComboBox")
        self.searchColumnComboBox.setMinimumSize(QSize(150, 36))
        self.searchColumnComboBox.setStyleSheet(u"\n"
"                QComboBox {\n"
"                    background-color: #FFFFFF;\n"
"                    border: 1px solid #B0B0B0;\n"
"                    border-radius: 6px;\n"
"                    padding: 8px;\n"
"                    color: #333333;\n"
"                    font: 10pt \"Segoe UI\";\n"
"                }\n"
"                QComboBox:hover {\n"
"                    border: 1px solid #909090;\n"
"                }\n"
"                QComboBox:focus {\n"
"                    border: 1px solid #4A90E2;\n"
"                }\n"
"                QComboBox::drop-down {\n"
"                    subcontrol-origin: padding;\n"
"                    subcontrol-position: top right;\n"
"                    width: 20px;\n"
"                    border-left: 1px solid #B0B0B0;\n"
"                    border-top-right-radius: 6px;\n"
"                    border-bottom-right-radius: 6px;\n"
"                }\n"
"                QComboBox::down-arrow {\n"
"                    image: url(:/icons/down-arrow."
                        "png);\n"
"                }\n"
"             ")

        self.buttonLayout.addWidget(self.searchColumnComboBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer_2)

        self.sortLabel = QLabel(self.main_page)
        self.sortLabel.setObjectName(u"sortLabel")
        self.sortLabel.setStyleSheet(u"\n"
"                QLabel {\n"
"                    color: #333333;\n"
"                    font: 10pt \"Segoe UI\";\n"
"                    padding: 8px;\n"
"                }\n"
"             ")

        self.buttonLayout.addWidget(self.sortLabel)

        self.sortOrderComboBox = QComboBox(self.main_page)
        self.sortOrderComboBox.addItem("")
        self.sortOrderComboBox.addItem("")
        self.sortOrderComboBox.setObjectName(u"sortOrderComboBox")
        self.sortOrderComboBox.setMinimumSize(QSize(150, 36))
        self.sortOrderComboBox.setStyleSheet(u"\n"
"                QComboBox {\n"
"                    background-color: #FFFFFF;\n"
"                    border: 1px solid #B0B0B0;\n"
"                    border-radius: 6px;\n"
"                    padding: 8px;\n"
"                    color: #333333;\n"
"                    font: 10pt \"Segoe UI\";\n"
"                }\n"
"                QComboBox:hover {\n"
"                    border: 1px solid #909090;\n"
"                }\n"
"                QComboBox:focus {\n"
"                    border: 1px solid #4A90E2;\n"
"                }\n"
"                QComboBox::drop-down {\n"
"                    subcontrol-origin: padding;\n"
"                    subcontrol-position: top right;\n"
"                    width: 20px;\n"
"                    border-left: 1px solid #B0B0B0;\n"
"                    border-top-right-radius: 6px;\n"
"                    border-bottom-right-radius: 6px;\n"
"                }\n"
"                QComboBox::down-arrow {\n"
"                    image: url(:/icons/down-arrow."
                        "png);\n"
"                }\n"
"             ")

        self.buttonLayout.addWidget(self.sortOrderComboBox)

        self.sortColumnComboBox = QComboBox(self.main_page)
        self.sortColumnComboBox.setObjectName(u"sortColumnComboBox")
        self.sortColumnComboBox.setMinimumSize(QSize(150, 36))
        self.sortColumnComboBox.setStyleSheet(u"\n"
"                QComboBox {\n"
"                    background-color: #FFFFFF;\n"
"                    border: 1px solid #B0B0B0;\n"
"                    border-radius: 6px;\n"
"                    padding: 8px;\n"
"                    color: #333333;\n"
"                    font: 10pt \"Segoe UI\";\n"
"                }\n"
"                QComboBox:hover {\n"
"                    border: 1px solid #909090;\n"
"                }\n"
"                QComboBox:focus {\n"
"                    border: 1px solid #4A90E2;\n"
"                }\n"
"                QComboBox::drop-down {\n"
"                    subcontrol-origin: padding;\n"
"                    subcontrol-position: top right;\n"
"                    width: 20px;\n"
"                    border-left: 1px solid #B0B0B0;\n"
"                    border-top-right-radius: 6px;\n"
"                    border-bottom-right-radius: 6px;\n"
"                }\n"
"                QComboBox::down-arrow {\n"
"                    image: url(:/icons/down-arrow."
                        "png);\n"
"                }\n"
"             ")

        self.buttonLayout.addWidget(self.sortColumnComboBox)


        self.verticalLayout_2.addLayout(self.buttonLayout)

        self.tableView = QTableView(self.main_page)
        self.tableView.setObjectName(u"tableView")
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setStyleSheet(u" QTableView {\n"
"                background-color: #FFFFFF;\n"
"                border: 1px solid #D3D3D3;\n"
"                gridline-color: #E0E0E0;\n"
"                font: 9pt \"Segoe UI\";\n"
"                color: #333333;\n"
"                border-radius: 6px;\n"
"                padding: 4px;\n"
"            }\n"
"            QTableView::item {\n"
"                padding: 8px;\n"
"                white-space: normal;\n"
"                word-wrap: break-word;\n"
"                text-align: center;\n"
"            }\n"
"            QTableView::item:nth-child(even) {\n"
"                background-color: #F9FAFB;\n"
"            }\n"
"            QTableView::item:nth-child(odd) {\n"
"                background-color: #FFFFFF;\n"
"            }\n"
"            QTableView::item:selected {\n"
"                background-color: #4A90E2;\n"
"                color: #FFFFFF;\n"
"                border: 1px solid #357ABD;\n"
"            }\n"
"QHeaderView::section {\n"
"    background-color: qlineargradie"
                        "nt(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #E8F5E9, stop:1 #D4EFDF);\n"
"    color: #333333;\n"
"    font: bold 10pt \"Segoe UI\";\n"
"    padding: 8px;\n"
"    border: 1px solid #A0A0B0;\n"
"    border-bottom: 2px solid #78909C;\n"
"    text-align: center;\n"
"    min-height: 40px;\n"
"  }\n"
"            QHeaderView::section:first {\n"
"                border-left: 1px solid #D3D3D3;\n"
"            }\n"
"            QHeaderView::section:last {\n"
"                border-right: 1px solid #D3D3D3;\n"
"            }\n"
"            QScrollBar:vertical, QScrollBar:horizontal {\n"
"                background: #F0F0F0;\n"
"                border: 1px solid #D3D3D3;\n"
"                border-radius: 4px;\n"
"            }\n"
"            QScrollBar::handle {\n"
"                background: #B0B0B0;\n"
"                border-radius: 4px;\n"
"            }\n"
"            QScrollBar::handle:hover {\n"
"                background: #909090;\n"
"            }")

        self.verticalLayout_2.addWidget(self.tableView)

        self.stackedWidget.addWidget(self.main_page)
        self.event_page = QWidget()
        self.event_page.setObjectName(u"event_page")
        self.verticalLayout_events = QVBoxLayout(self.event_page)
        self.verticalLayout_events.setSpacing(12)
        self.verticalLayout_events.setObjectName(u"verticalLayout_events")
        self.verticalLayout_events.setContentsMargins(12, 12, 12, 12)
        self.eventButtonLayout = QHBoxLayout()
        self.eventButtonLayout.setSpacing(8)
        self.eventButtonLayout.setObjectName(u"eventButtonLayout")
        self.create_event_button = QPushButton(self.event_page)
        self.create_event_button.setObjectName(u"create_event_button")
        self.create_event_button.setMinimumSize(QSize(140, 36))
        self.create_event_button.setStyleSheet(u"\n"
"                QPushButton {\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4A90E2, stop:1 #357ABD);\n"
"                    color: #FFFFFF;\n"
"                    border: none;\n"
"                    border-radius: 6px;\n"
"                    padding: 10px;\n"
"                    font: bold 10pt \"Segoe UI\";\n"
"                }\n"
"                QPushButton:hover {\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #357ABD, stop:1 #2D5D9F);\n"
"                }\n"
"                QPushButton:pressed {\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #2D5D9F, stop:1 #254C80);\n"
"                }\n"
"                QPushButton:disabled {\n"
"                    background-color: #CCCCCC;\n"
"                    color: #666666;\n"
"                }\n"
"             ")

        self.eventButtonLayout.addWidget(self.create_event_button)

        self.edit_event_button = QPushButton(self.event_page)
        self.edit_event_button.setObjectName(u"edit_event_button")
        self.edit_event_button.setMinimumSize(QSize(140, 36))
        self.edit_event_button.setStyleSheet(u"\n"
"                QPushButton {\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4A90E2, stop:1 #357ABD);\n"
"                    color: #FFFFFF;\n"
"                    border: none;\n"
"                    border-radius: 6px;\n"
"                    padding: 10px;\n"
"                    font: bold 10pt \"Segoe UI\";\n"
"                }\n"
"                QPushButton:hover {\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #357ABD, stop:1 #2D5D9F);\n"
"                }\n"
"                QPushButton:pressed {\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #2D5D9F, stop:1 #254C80);\n"
"                }\n"
"                QPushButton:disabled {\n"
"                    background-color: #CCCCCC;\n"
"                    color: #666666;\n"
"                }\n"
"             ")

        self.eventButtonLayout.addWidget(self.edit_event_button)

        self.delete_event_button = QPushButton(self.event_page)
        self.delete_event_button.setObjectName(u"delete_event_button")
        self.delete_event_button.setMinimumSize(QSize(140, 36))
        self.delete_event_button.setStyleSheet(u"\n"
"                QPushButton {\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #E24A4A, stop:1 #BD3535);\n"
"                    color: #FFFFFF;\n"
"                    border: none;\n"
"                    border-radius: 6px;\n"
"                    padding: 10px;\n"
"                    font: bold 10pt \"Segoe UI\";\n"
"                }\n"
"                QPushButton:hover {\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #BD3535, stop:1 #9F2D2D);\n"
"                }\n"
"                QPushButton:pressed {\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #9F2D2D, stop:1 #802525);\n"
"                }\n"
"                QPushButton:disabled {\n"
"                    background-color: #CCCCCC;\n"
"                    color: #666666;\n"
"                }\n"
"             ")

        self.eventButtonLayout.addWidget(self.delete_event_button)

        self.horizontalSpacer_events = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.eventButtonLayout.addItem(self.horizontalSpacer_events)


        self.verticalLayout_events.addLayout(self.eventButtonLayout)

        self.eventTableView = QTableView(self.event_page)
        self.eventTableView.setObjectName(u"eventTableView")
        sizePolicy.setHeightForWidth(self.eventTableView.sizePolicy().hasHeightForWidth())
        self.eventTableView.setSizePolicy(sizePolicy)
        self.eventTableView.setStyleSheet(u"\n"
"            QTableView {\n"
"                background-color: #FFFFFF;\n"
"                border: 1px solid #D3D3D3;\n"
"                gridline-color: #E0E0E0;\n"
"                font: 9pt \"Segoe UI\";\n"
"                color: #333333;\n"
"                border-radius: 6px;\n"
"                padding: 4px;\n"
"            }\n"
"            QTableView::item {\n"
"                padding: 8px;\n"
"                white-space: normal;\n"
"                word-wrap: break-word;\n"
"                text-align: center;\n"
"            }\n"
"            QTableView::item:nth-child(even) {\n"
"                background-color: #F9FAFB;\n"
"            }\n"
"            QTableView::item:nth-child(odd) {\n"
"                background-color: #FFFFFF;\n"
"            }\n"
"            QTableView::item:selected {\n"
"                background-color: #4A90E2;\n"
"                color: #FFFFFF;\n"
"                border: 1px solid #357ABD;\n"
"            }\n"
"            QHeaderView::section {\n"
"       "
                        "         background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #E2E8F0, stop:1 #D3DCE5);\n"
"                color: #333333;\n"
"                font: bold 10pt \"Segoe UI\";\n"
"                padding: 8px;\n"
"                border: 1px solid #D3D3D3;\n"
"                border-right: none;\n"
"                border-bottom: 2px solid #B0B0B0;\n"
"                text-align: center;\n"
"            }\n"
"            QHeaderView::section:first {\n"
"                border-left: 1px solid #D3D3D3;\n"
"            }\n"
"            QHeaderView::section:last {\n"
"                border-right: 1px solid #D3D3D3;\n"
"            }\n"
"            QScrollBar:vertical, QScrollBar:horizontal {\n"
"                background: #F0F0F0;\n"
"                border: 1px solid #D3D3D3;\n"
"                border-radius: 4px;\n"
"            }\n"
"            QScrollBar::handle {\n"
"                background: #B0B0B0;\n"
"                border-radius: 4px;\n"
"            }\n"
"            QScro"
                        "llBar::handle:hover {\n"
"                background: #909090;\n"
"            }\n"
"           ")

        self.verticalLayout_events.addWidget(self.eventTableView)

        self.stackedWidget.addWidget(self.event_page)
        self.backups_page = QWidget()
        self.backups_page.setObjectName(u"backups_page")
        self.backups_page.setStyleSheet(u"\n"
"         QWidget {\n"
"             background-color: #FFFFFF;\n"
"             border: 1px solid #D3D3D3;\n"
"             border-radius: 8px;\n"
"             padding: 8px;\n"
"         }\n"
"        ")
        self.stackedWidget.addWidget(self.backups_page)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"\n"
"     QStatusBar {\n"
"         background-color: #F0F0F0;\n"
"         color: #333333;\n"
"         font: 9pt \"Segoe UI\";\n"
"         border-top: 1px solid #D3D3D3;\n"
"         padding: 4px;\n"
"     }\n"
"    ")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MedShed", None))
        self.main_button.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.event_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0431\u044b\u0442\u0438\u044f", None))
        self.backups_button.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0435\u0440\u0432\u043d\u044b\u0435\n"
"\u043a\u043e\u043f\u0438\u0438", None))
        self.export_button.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.import_button.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442", None))
        self.guide_button.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e", None))
        self.create_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.edit_button.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.searchLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a:", None))
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u0430\u043f\u0440\u043e\u0441 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430...", None))
        self.sortLabel.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c:", None))
        self.sortOrderComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u0430\u043d\u0438\u044e", None))
        self.sortOrderComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0443\u0431\u044b\u0432\u0430\u043d\u0438\u044e", None))

        self.create_event_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0441\u043e\u0431\u044b\u0442\u0438\u0435", None))
        self.edit_event_button.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0441\u043e\u0431\u044b\u0442\u0438\u0435", None))
        self.delete_event_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u043e\u0431\u044b\u0442\u0438\u0435", None))
    # retranslateUi

