import os

from PyQt5.QtWidgets import QApplication
from pyqt_dark_calculator.calculator import Calculator

from pyqt_new_window_handler import NewWindowHandler


class CalculatorApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        icon_filename = os.path.join(os.path.dirname(__file__), 'ico/calculator.svg')
        self.__handler = NewWindowHandler(Calculator, icon_filename=icon_filename)