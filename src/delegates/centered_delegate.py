from PySide6.QtWidgets import QItemDelegate
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPainter, QTextOption, QTextDocument
from utils.text_utils import insert_soft_hyphens

class CenteredDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, index):
        painter.save()
        option.displayAlignment = Qt.AlignCenter
        text_option = QTextOption(Qt.AlignCenter)
        text_option.setWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)
        option.textOption = text_option
        option.elideMode = Qt.ElideNone
        
        text = index.data(Qt.DisplayRole)
        text = insert_soft_hyphens(text)
        option.text = text
        
        super().paint(painter, option, index)
        painter.restore()

    def sizeHint(self, option, index):
        text = index.data(Qt.DisplayRole)
        text = insert_soft_hyphens(text) or ""
        
        doc = QTextDocument()
        doc.setDefaultFont(option.font)
        doc.setTextWidth(option.rect.width())
        doc.setDocumentMargin(4)
        text_option = QTextOption(Qt.AlignCenter)
        text_option.setWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)
        doc.setDefaultTextOption(text_option)
        doc.setHtml(f"<div style='text-align: center'>{text}</div>")
        
        size = QSize(int(doc.idealWidth() + 8), int(doc.size().height() + 8))
        return size