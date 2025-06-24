from PySide6.QtWidgets import QHeaderView, QStyleOptionHeader
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QTextOption, QTextDocument
from PySide6.QtWidgets import QStyle
from utils.text_utils import insert_soft_hyphens

class CustomHeaderView(QHeaderView):
    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self.setDefaultAlignment(Qt.AlignCenter)
        self.setStyleSheet(parent.styleSheet())
        self.setSectionsClickable(True)
        self._text_cache = {}

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()

        opt = QStyleOptionHeader()
        self.initStyleOption(opt)
        opt.rect = rect
        opt.section = logicalIndex
        opt.text = ""
        style = self.style()
        style.drawControl(QStyle.CE_Header, opt, painter, self)

        text = self.model().headerData(logicalIndex, self.orientation(), Qt.DisplayRole)
        if not text:
            painter.restore()
            return

        section_width = self.sectionSize(logicalIndex) - 16
        if section_width <= 0:
            section_width = 100

        cache_key = (logicalIndex, section_width, text)
        if cache_key not in self._text_cache:
            doc = QTextDocument()
            doc.setDefaultFont(self.font())
            doc.setTextWidth(section_width)
            text_option = QTextOption(Qt.AlignCenter)
            text_option.setWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)
            doc.setDefaultTextOption(text_option)
            doc.setDocumentMargin(0)
            formatted_text = insert_soft_hyphens(str(text))
            doc.setHtml(f"<div style='text-align: center'>{formatted_text}</div>")
            self._text_cache[cache_key] = doc
        else:
            doc = self._text_cache[cache_key]

        painter.translate(rect.left() + 8, rect.top() + 8)
        clip_rect = QRect(0, 0, section_width, rect.height() - 16)
        painter.setClipRect(clip_rect)
        doc.drawContents(painter)

        painter.restore()

    def sizeHint(self):
        size = super().sizeHint()
        max_height = 40

        for i in range(self.count()):
            text = self.model().headerData(i, self.orientation(), Qt.DisplayRole)
            if text:
                section_width = self.sectionSize(i) - 16
                if section_width <= 0:
                    section_width = 100

                doc = QTextDocument()
                doc.setDefaultFont(self.font())
                doc.setTextWidth(section_width)
                text_option = QTextOption(Qt.AlignCenter)
                text_option.setWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)
                doc.setDefaultTextOption(text_option)
                doc.setDocumentMargin(0)
                formatted_text = insert_soft_hyphens(str(text))
                doc.setHtml(f"<div style='text-align: center'>{formatted_text}</div>")

                section_height = int(doc.size().height()) + 16
                max_height = max(max_height, section_height)

        size.setHeight(max_height)
        return size