from PyQt5.QtWidgets import QApplication, QAbstractButton
from pyqt_dark_calculator.calculator import Calculator

from pyqt_style_setter import StyleSetter
from pyqt_custom_titlebar_setter import CustomTitlebarSetter
from pyqt_custom_titlebar_window import CustomTitlebarWindow


class CalculatorApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.installEventFilter(self)
        self.__windowDict = dict()
        self.__new()

    def __new(self):
        mainWindow = Calculator()
        mainWindow.newClicked.connect(self.__new)
        StyleSetter.setWindowStyle(mainWindow, exclude_type_lst=[QAbstractButton])
        titleBarWindow = CustomTitlebarSetter.getCustomTitleBar(mainWindow, icon_filename='ico/calculator.svg')
        titleBarWindow.show()

    def eventFilter(self, obj, e):
        if isinstance(obj, CustomTitlebarWindow):
            if e.type() == 17:
                self.__windowDict[obj] = obj.winId()
            elif e.type() == 19:
                w = self.__windowDict.get(obj, 0)
                if w:
                    self.__windowDict.pop(obj)
        return super().eventFilter(obj, e)