from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea
from PyQt5.QtCore import Qt


class ResultWidget(QScrollArea):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        lay = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(lay)
        self.setMinimumHeight(self.window().height()//3)
        self.setWidget(widget)
        self.setWidgetResizable(True)

        # style of the resultWidget (if you have to change the style of this just change as you want)
        self.setStyleSheet('QWidget { background-color: #333; border: none; }')

    def setText(self, formula_text: str, value_text: str) -> None:
        formula_lbl = QLabel()
        formula_lbl.setText(formula_text)
        formula_lbl.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        formula_lbl.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)

        value_lbl = QLabel()
        value_lbl.setText(value_text)
        value_lbl.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        value_lbl.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)

        font = value_lbl.font()
        font.setPixelSize(20)
        value_lbl.setFont(font)

        self.widget().layout().addWidget(formula_lbl, stretch=1)
        self.widget().layout().addWidget(value_lbl)

    def resizeEvent(self, e):
        self.setMinimumHeight(self.window().height()//3)
        return super().resizeEvent(e)

    def event(self, e):
        if e.type() == 43:
            self.verticalScrollBar().setSliderPosition(self.verticalScrollBar().maximum())
        return super().event(e)

    def count(self):
        lay = self.widget().layout()
        return lay.count()

    def getLastText(self):
        lay = self.widget().layout()
        return lay.itemAt(lay.count()-1).widget().text()

    def clear(self):
        lay = self.widget().layout()
        for i in range(lay.count()-1, -1, -1):
            lay.removeWidget(lay.itemAt(i).widget())