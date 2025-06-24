from PySide6.QtWidgets import QMenu, QStyle
import logging

logger = logging.getLogger(__name__)

def on_equipment_context_menu(window, pos):
    if not window.ui.tableView.selectedIndexes():
        logger.debug("Контекстное меню: нет выбранных строк")
        return
    style = window.style()
    edit_icon = style.standardIcon(QStyle.StandardPixmap.SP_FileDialogDetailedView)
    delete_icon = style.standardIcon(QStyle.StandardPixmap.SP_TrashIcon)
    apply_icon = style.standardIcon(QStyle.StandardPixmap.SP_DialogApplyButton)

    actions_info = [
        (edit_icon, "Изменить", window.edit_selected_equipment),
        (delete_icon, "Удалить", window.delete_selected_equipment),
        (apply_icon, "Отметить поверку сегодня", window.mark_verification_today),
    ]
    logger.debug("Контекстное меню открывается")
    show_context_menu(window, pos, window.ui.tableView, actions_info)

def on_event_context_menu(window, pos):
    if not window.ui.eventTableView.selectedIndexes():
        logger.debug("Контекстное меню: нет выбранных строк")
        return
    style = window.style()
    edit_icon = style.standardIcon(QStyle.StandardPixmap.SP_FileDialogDetailedView)
    delete_icon = style.standardIcon(QStyle.StandardPixmap.SP_TrashIcon)

    actions_info = [
        (edit_icon, "Изменить событие", window.edit_selected_event),
        (delete_icon, "Удалить событие", window.delete_selected_event),
    ]
    show_context_menu(window, pos, window.ui.eventTableView, actions_info)

def show_context_menu(window, pos, widget, actions_info):
    menu = QMenu(window)

    menu.setStyleSheet("""
        QMenu {
            background-color: #ffffff;
            color: #000000;
            border: 1px solid #cccccc;
            padding: 5px;
        }
        QMenu::item {
            background-color: transparent;
            color: #000000;
            padding: 5px 20px;
        }
        QMenu::item:selected {
            background-color: #0078d7;
            color: #ffffff;
        }
    """)

    actions = []
    for icon, text, handler in actions_info:
        action = menu.addAction(icon, text)
        actions.append((action, handler))

    action = menu.exec(widget.mapToGlobal(pos))
    if action:
        for act, handler in actions:
            if action == act:
                handler()
                break