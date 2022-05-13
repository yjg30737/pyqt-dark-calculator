from PyQt5.QtWidgets import QApplication
from pyqt_dark_calculator.calculator import Calculator

import absresgetter
from pyqt_new_window_handler import NewWindowHandler


class CalculatorApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__handler = NewWindowHandler(Calculator, absresgetter.getabsres('ico/calculator.svg'))