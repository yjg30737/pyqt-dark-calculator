from PyQt5.QtWidgets import QApplication, QAbstractButton
from pyqt_dark_calculator.calculator import Calculator

from python_get_absolute_resource_path import get_absolute_resource_path
from pyqt_new_window_handler import NewWindowHandler


class CalculatorApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__handler = NewWindowHandler(Calculator, get_absolute_resource_path('ico/calculator.svg'),
                                          exclude_type_lst=[QAbstractButton])