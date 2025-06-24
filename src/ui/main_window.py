from datetime import datetime
from PySide6.QtWidgets import QMainWindow, QMessageBox, QAbstractItemView, QFileDialog, QHeaderView
from PySide6.QtCore import Qt, QSettings, QTimer, QUrl
from PySide6.QtGui import QIcon, QDesktopServices, QTransform
from sqlalchemy import inspect
import sys
import logging
from ui.interface_ui import Ui_MainWindow
from bd.data_base_manager import DataBaseManager
from bd.equipment_table_model import EquipmentTableModel
from bd.calibration_event_table_model import CalibrationEventTableModel
from delegates.centered_delegate import CenteredDelegate
from delegates.custom_header_view import CustomHeaderView
from delegates.custom_sort_filter_proxy import CustomSortFilterProxyModel
from utils.path_utils import resource_path
from handlers.equipment_handlers import create_equipment, edit_equipment, delete_equipment, mark_verification_today
from handlers.event_handlers import create_event, edit_event, delete_event
from handlers.import_handlers import import_from_excel, import_from_pdf
from handlers.export_handlers import export_data
from handlers.context_menu_handlers import show_context_menu, on_equipment_context_menu, on_event_context_menu
from utils.date_utils import parse_date

logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_equipment = None
        self.current_calibration_event = None
        self.last_selected_row = None
        self.last_selected_event_row = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        icon_path = resource_path('res/icons/icon.ico')
        self.setWindowIcon(QIcon(icon_path))
        self.setWindowTitle("SchedMed")

        btn = self.ui.import_button
        icon = btn.icon()
        pixmap = icon.pixmap(btn.iconSize())
        transform = QTransform().scale(-1, 1)
        mirrored_pixmap = pixmap.transformed(transform)
        btn.setIcon(QIcon(mirrored_pixmap))
        QTimer.singleShot(0, self.showMaximized)

        self.search_timer = QTimer(self)
        self.search_timer.setSingleShot(True)
        self.search_timer.timeout.connect(self.apply_search)

        self.setup_handlers()
        self.ui.stackedWidget.setCurrentIndex(0)

        self.db_manager = DataBaseManager()
        self.session_manager = self.db_manager.get_session()

        try:
            from bd.equipment_model import Base
            Base.metadata.create_all(self.session_manager.bind)
            inspector = inspect(self.session_manager.bind)
            tables = inspector.get_table_names()
            logger.debug(f"Таблицы в базе данных: {tables}")
            if not all(table in tables for table in ['equipment', 'events']):
                logger.error("Не все таблицы созданы")
                self.show_error("Ошибка", "Не удалось создать все таблицы")
                sys.exit(1)
            columns = [col['name'] for col in inspector.get_columns('equipment')]
            logger.debug(f"Колонки таблицы equipment: {columns}")
            event_columns = [col['name'] for col in inspector.get_columns('events')]
            logger.debug(f"Колонки таблицы events: {event_columns}")
        except Exception as e:
            logger.error(f"Ошибка создания таблиц: {str(e)}")
            self.show_error("Ошибка", f"Ошибка создания таблиц: {str(e)}")
            sys.exit(1)

        self.model = EquipmentTableModel(self.session_manager)
        self.proxy_model = CustomSortFilterProxyModel(self)
        self.proxy_model.setSourceModel(self.model)
        self.ui.tableView.setModel(self.proxy_model)
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableView.setHorizontalHeader(CustomHeaderView(Qt.Horizontal, self.ui.tableView))
        self.ui.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.tableView.setWordWrap(True)
        self.ui.tableView.setTextElideMode(Qt.ElideNone)
        self.ui.tableView.resizeRowsToContents()
        self.ui.tableView.verticalHeader().hide()
        self.ui.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tableView.setItemDelegate(CenteredDelegate(self.ui.tableView))

        settings = QSettings("MyApp", "SchedMed")
        default_widths = [50, 200, 100, 100, 150, 100, 100, 100, 250, 100, 150]
        column_count = self.model.columnCount()
        header = self.ui.tableView.horizontalHeader()

        header.setSectionResizeMode(QHeaderView.Interactive)

        total_width = self.ui.tableView.viewport().width()
        if total_width <= 0:
            total_width = self.ui.tableView.width() - 20
        total_default_width = sum(default_widths[:column_count])
        scale_factor = total_width / total_default_width if total_default_width > 0 else 1.0

        for i in range(column_count):
            saved_width = settings.value(f"column_width_{i}", default_widths[i] * scale_factor, type=int)
            self.ui.tableView.setColumnWidth(i, int(saved_width))

        header.sectionResized.connect(self.save_column_widths)

        self.init_search()
        self.init_sorting()

        self.event_model = CalibrationEventTableModel(self.session_manager)
        self.ui.eventTableView.setModel(self.event_model)
        self.ui.eventTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.eventTableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.eventTableView.setHorizontalHeader(CustomHeaderView(Qt.Horizontal, self.ui.eventTableView))
        self.ui.eventTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.eventTableView.setWordWrap(True)
        self.ui.eventTableView.resizeRowsToContents()
        self.ui.eventTableView.verticalHeader().hide()
        self.ui.eventTableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.eventTableView.setItemDelegate(CenteredDelegate(self.ui.eventTableView))
        for i in range(self.event_model.columnCount()):
            self.ui.eventTableView.setColumnWidth(i, 150)

    def init_search(self):
        self.ui.searchColumnComboBox.clear()
        self.ui.searchColumnComboBox.addItem("Все колонки")
        for header in self.model.headers[1:]:
            self.ui.searchColumnComboBox.addItem(header)

    def init_sorting(self):
        self.ui.sortOrderComboBox.setCurrentIndex(0)
        column_names = self.model.headers
        self.ui.sortColumnComboBox.addItems(column_names)
        self.ui.sortColumnComboBox.setCurrentIndex(0)

        self.ui.sortOrderComboBox.currentIndexChanged.connect(self.apply_sorting)
        self.ui.sortColumnComboBox.currentIndexChanged.connect(self.apply_sorting)

        self.apply_sorting()

    def apply_sorting(self):
        column_index = self.ui.sortColumnComboBox.currentIndex()
        order_text = self.ui.sortOrderComboBox.currentText()
        order = Qt.AscendingOrder if order_text == "По возрастанию" else Qt.DescendingOrder

        logger.debug(f"Сортировка: колонка={column_index}, порядок={order_text}")
        self.proxy_model.sort(column_index, order)
        self.last_selected_row = None
        self.last_selected_event_row = None

    def apply_search(self):
        logger.debug(f"Применение поиска: текст={self.ui.searchLineEdit.text()}, колонка={self.ui.searchColumnComboBox.currentText()}")
        try:
            from PySide6.QtCore import QRegularExpression
            search_text = self.ui.searchLineEdit.text()
            column = self.ui.searchColumnComboBox.currentText()
            column_index = self.ui.searchColumnComboBox.currentIndex()

            reg_exp = QRegularExpression(search_text, QRegularExpression.CaseInsensitiveOption)

            if column == "Все колонки":
                self.proxy_model.setFilterRegularExpression(reg_exp)
                self.proxy_model.setFilterKeyColumn(-1)
            else:
                self.proxy_model.setFilterKeyColumn(column_index)
                self.proxy_model.setFilterRegularExpression(reg_exp)

            self.ui.tableView.resizeRowsToContents()
            self.apply_sorting()
        except Exception as e:
            logger.error(f"Ошибка при поиске: {str(e)}")
            self.show_error("Ошибка", f"Ошибка при поиске: {str(e)}")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjust_column_widths()

    def adjust_column_widths(self):
        total_width = self.ui.tableView.viewport().width()
        if total_width <= 0:
            total_width = self.ui.tableView.width() - 20
        column_count = self.model.columnCount()
        settings = QSettings("MyApp", "SchedMed")
        default_widths = [50, 200, 100, 100, 150, 100, 100, 100, 250, 100, 150]
        total_default_width = sum(default_widths[:column_count])
        scale_factor = total_width / total_default_width if total_default_width > 0 else 1.0

        current_widths = []
        for i in range(column_count):
            saved_width = settings.value(f"column_width_{i}", default_widths[i] * scale_factor, type=int)
            current_widths.append(saved_width)
        
        total_current_width = sum(current_widths)
        if total_current_width > 0:
            scale_factor = total_width / total_current_width
            for i in range(column_count):
                new_width = int(current_widths[i] * scale_factor)
                self.ui.tableView.setColumnWidth(i, max(50, new_width))

    def save_column_widths(self, logicalIndex, oldSize, newSize):
        settings = QSettings("MyApp", "SchedMed")
        settings.setValue(f"column_width_{logicalIndex}", newSize)
        logger.debug(f"Ширина колонки {logicalIndex} сохранена: {newSize}")

    def closeEvent(self, event):
        settings = QSettings("MyApp", "SchedMed")
        for i in range(self.model.columnCount()):
            width = self.ui.tableView.columnWidth(i)
            settings.setValue(f"column_width_{i}", width)
        logger.debug("Ширины колонок сохранены")
        super().closeEvent(event)

    def setup_handlers(self):
        try:
            self.ui.main_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
            self.ui.event_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
            self.ui.backups_button.clicked.connect(self.open_backups_dialog)
            self.ui.export_button.clicked.connect(self.open_export_dialog)
            self.ui.import_button.clicked.connect(self.open_import_dialog)
            self.ui.create_button.clicked.connect(self.on_create_button_clicked)
            self.ui.edit_button.clicked.connect(self.edit_selected_equipment)
            self.ui.delete_button.clicked.connect(self.delete_selected_equipment)
            self.ui.create_event_button.clicked.connect(self.create_event)
            self.ui.edit_event_button.clicked.connect(self.edit_selected_event)
            self.ui.delete_event_button.clicked.connect(self.delete_selected_event)
            self.ui.tableView.customContextMenuRequested.connect(self.on_equipment_context_menu)
            self.ui.eventTableView.customContextMenuRequested.connect(self.on_event_context_menu)
            self.ui.tableView.clicked.connect(self.on_row_clicked)
            self.ui.eventTableView.clicked.connect(self.on_event_row_clicked)
            self.ui.tableView.doubleClicked.connect(self.on_row_double_clicked)
            self.ui.tableView.horizontalHeader().sectionResized.connect(self.ui.tableView.resizeRowsToContents)
            self.ui.eventTableView.horizontalHeader().sectionResized.connect(self.ui.eventTableView.resizeRowsToContents)
            self.ui.searchLineEdit.textChanged.connect(self.on_search_text_changed)
            self.ui.searchColumnComboBox.currentTextChanged.connect(self.on_search_text_changed)
            self.ui.guide_button.clicked.connect(self.open_user_guide)
        except AttributeError as e:
            logger.error(f"Ошибка подключения обработчиков: {str(e)}")
            self.show_error("Ошибка", f"Ошибка подключения обработчиков: {str(e)}")

    def on_search_text_changed(self, text=None):
        logger.debug(f"Поисковый запрос получен: текст={self.ui.searchLineEdit.text()}, колонка={self.ui.searchColumnComboBox.currentText()}")
        self.search_timer.start(300)

    def open_import_dialog(self):
        logger.debug("Открытие диалога выбора формата импорта")
        from ui.import_format_dialog import ImportFormatDialog
        dialog = ImportFormatDialog(self)
        if dialog.exec():
            selected_format = dialog.selected_format
            replace_table = dialog.replace_table
            if selected_format:
                file_dialog = QFileDialog(self)
                file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
                file_dialog.setNameFilter(f"{selected_format.upper()} Files (*.{selected_format})")
                if file_dialog.exec():
                    file_path = file_dialog.selectedFiles()[0]
                    logger.debug(f"Выбран файл для импорта: {file_path}, формат: {selected_format}, режим: {'Замена' if replace_table else 'Добавление'}")
                    if selected_format == "xlsx":
                        import_from_excel(self, file_path, replace_table)
                    elif selected_format == "pdf":
                        import_from_pdf(self, file_path, replace_table)
                else:
                    logger.debug("Выбор файла для импорта отменён")
        else:
            logger.debug("Импорт отменён пользователем")

    def open_user_guide(self):
        guide_path = resource_path('res/user_guide/user_guide.html')
        QDesktopServices.openUrl(QUrl.fromLocalFile(guide_path))

    def open_export_dialog(self):
        logger.debug("Открытие диалога выбора формата экспорта")
        from ui.export_format_dialog import ExportFormatDialog
        dialog = ExportFormatDialog(self)
        if dialog.exec():
            selected_format = dialog.selected_format
            if selected_format:
                export_data(self, selected_format)
        else:
            logger.debug("Экспорт отменён пользователем")

    def open_backups_dialog(self):
        logger.debug("Открытие диалога резервного копирования")
        from ui.backups_dialog import BackupsDialog
        dialog = BackupsDialog(self)
        dialog.exec()

    def on_row_clicked(self, index):
        row = index.row()
        try:
            if 0 <= row < self.proxy_model.rowCount():
                if self.last_selected_row == row:
                    self.ui.tableView.clearSelection()
                    self.current_equipment = None
                    self.last_selected_row = None
                    logger.debug(f"Выделение снято с записи в строке {row}")
                else:
                    source_index = self.proxy_model.mapToSource(index)
                    equipment = self.model.get_equipment(source_index.row())
                    if equipment:
                        self.current_equipment = equipment
                        self.last_selected_row = row
                        logger.debug(f"Выбрана запись: {equipment.equipment_name} (ID: {equipment.id})")
                    else:
                        self.current_equipment = None
                        self.last_selected_row = None
                        logger.debug("Запись не найдена")
            else:
                self.current_equipment = None
                self.last_selected_row = None
                logger.debug("Выбранная строка вне диапазона")
        except Exception as e:
            logger.error(f"Ошибка доступа к данным: {str(e)}")
            self.show_error("Ошибка", f"Ошибка доступа к данным: {str(e)}")

    def on_event_row_clicked(self, index):
        row = index.row()
        try:
            if 0 <= row < self.event_model.rowCount():
                if self.last_selected_event_row == row:
                    self.ui.eventTableView.clearSelection()
                    self.current_calibration_event = None
                    self.last_selected_event_row = None
                    logger.debug(f"Выделение снято с события в строке {row}")
                else:
                    calibration_event = self.event_model.get_event(row)
                    if calibration_event:
                        self.current_calibration_event = calibration_event
                        self.last_selected_event_row = row
                        logger.debug(f"Выбрано событие: ID {calibration_event.id}, {calibration_event.check_days} дней")
                    else:
                        self.current_calibration_event = None
                        self.last_selected_event_row = None
                        logger.debug("Событие не найдена")
            else:
                self.current_calibration_event = None
                self.last_selected_event_row = None
                logger.debug("Выбранная строка вне диапазона")
        except Exception as e:
            logger.error(f"Ошибка доступа к данным события: {str(e)}")
            self.show_error("Ошибка", f"Ошибка доступа к данным события: {str(e)}")

    def on_row_double_clicked(self, index):
        row = index.row()
        try:
            if 0 <= row < self.proxy_model.rowCount():
                source_index = self.proxy_model.mapToSource(index)
                equipment = self.model.get_equipment(source_index.row())
                if equipment:
                    from ui.equipment_info_dialog import EquipmentInfoDialog
                    dialog = EquipmentInfoDialog(equipment, self.model, self)
                    dialog.exec()
                else:
                    self.show_error("Ошибка", "Запись не найдена")
            else:
                self.show_error("Ошибка", "Выбранная строка вне диапазона")
        except Exception as e:
            logger.error(f"Ошибка доступа к данным: {str(e)}")
            self.show_error("Ошибка", f"Ошибка доступа к данным: {str(e)}")

    def on_create_button_clicked(self):
        create_equipment(self)

    def edit_selected_equipment(self):
        edit_equipment(self)

    def delete_selected_equipment(self):
        delete_equipment(self)

    def create_event(self):
        create_event(self)

    def edit_selected_event(self):
        edit_event(self)

    def delete_selected_event(self):
        delete_event(self)

    def mark_verification_today(self):
        mark_verification_today(self)

    def on_equipment_context_menu(self, pos):
        on_equipment_context_menu(self, pos)

    def on_event_context_menu(self, pos):
        on_event_context_menu(self, pos)

    def show_context_menu(self, pos, widget, actions_info):
        show_context_menu(self, pos, widget, actions_info)

    def show_error(self, title, message):
        logger.error(f"{title}: {message}")
        
        error_box = QMessageBox(self)
        error_box.setIcon(QMessageBox.Critical)
        error_box.setWindowTitle(title)
        error_box.setText(message)
        error_box.setStandardButtons(QMessageBox.Ok)
        error_box.setDefaultButton(QMessageBox.Ok)
        error_box.setStyleSheet("""
            QMessageBox {
                background-color: #ffffff;
                color: #000000;
                font-size: 14px;
                font-family: Segoe UI, sans-serif;
                padding: 12px;
            }
            QPushButton {
                background-color: #d64541;
                color: white;
                padding: 6px 12px;
                border: none;
                border-radius: 4px;
                font-weight: bold;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        error_box.setWindowFlags(error_box.windowFlags() | Qt.WindowStaysOnTopHint)
        error_box.exec()

    def parse_date(self, value):
        return parse_date(value)