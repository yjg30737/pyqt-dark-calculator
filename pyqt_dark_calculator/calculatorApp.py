from PyQt5.QtWidgets import QApplication, QAbstractButton
from pyqt_dark_gray_theme.darkGrayTheme import *
from pyqt_dark_calculator.calculator import Calculator

from pyqt_style_setter import StyleSetter
from pyqt_custom_titlebar_setter import CustomTitlebarSetter


class CalculatorApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mainWindow = Calculator()
        StyleSetter.setWindowStyle(mainWindow, exclude_type_lst=[QAbstractButton])
        self.__titleBarWindow = CustomTitlebarSetter.getCustomTitleBar(mainWindow, icon_filename='ico/calculator.svg')
        self.__titleBarWindow.show()