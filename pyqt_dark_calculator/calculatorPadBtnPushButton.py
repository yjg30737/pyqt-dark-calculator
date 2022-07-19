from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QPushButton


class CalculatorPadBtnPushButton(QPushButton):
    padBtnClicked = pyqtSignal(str)

    def __init__(self, text):
        super().__init__(text)
        self.__initUi()

    def __initUi(self):
        font = self.font()
        font.setPixelSize(20)
        self.setFont(font)

    @pyqtSlot()
    def mousePressEvent(self, e):
        self.padBtnClicked.emit(self.text())
