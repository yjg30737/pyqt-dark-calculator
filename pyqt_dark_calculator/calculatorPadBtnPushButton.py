from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QPushButton


class CalculatorPadBtnPushButton(QPushButton):
    padBtnClicked = pyqtSignal(str)

    def __init__(self, text):
        super().__init__(text)

    @pyqtSlot()
    def mousePressEvent(self, e):
        self.padBtnClicked.emit(self.text())
