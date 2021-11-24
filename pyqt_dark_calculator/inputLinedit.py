import re

from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt, pyqtSignal, QRegExp


class InputLineEdit(QLineEdit):
    equalPressed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setAlignment(Qt.AlignRight)
        self.setValidator(QRegExpValidator(QRegExp("^[\d]+([\+\/\*\.\-\%][\(]?[\d]+[\)]?)*$")))
        font = self.font()
        font.setPixelSize(20)
        self.setFont(font)

    def getLastOperand(self):
        last_regex_n = re.search(r'(\d)+$', self.text())
        if last_regex_n:
            last_n = last_regex_n.group()
            return last_n
        return None

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Equal:
            self.equalPressed.emit()
        else:
            super().keyPressEvent(e)