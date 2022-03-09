from PyQt5.QtCore import Qt
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
        titleBarWindow.setAttribute(Qt.WA_DeleteOnClose)
        titleBarWindow.destroyed.connect(self.__destroyed)
        titleBarWindow.show()

    def eventFilter(self, obj, e):
        if isinstance(obj, CustomTitlebarWindow):
            # catch the QShowEvent of CustomTitlebarWindow
            if e.type() == 17:
                w = self.__getInnerWidget(obj)
                self.__windowDict[w] = obj
        return super().eventFilter(obj, e)

    def __destroyed(self, w):
        w = self.__getInnerWidget(w)
        del(self.__windowDict[w])

    def __getInnerWidget(self, w):
        inner_widget = [c for c in w.children() if isinstance(c, Calculator)][0]
        return inner_widget