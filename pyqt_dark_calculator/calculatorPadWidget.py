import os

from PyQt5.QtWidgets import QWidget, QGridLayout, QSizePolicy

from calculatorPadBtnPushButton import CalculatorPadBtnPushButton


class CalculatorPadWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__number_btns = []
        btn_texts = ['%', 'Rnd', 'C', 'CA', 'Del']+[7, 8, 9, '/', 'Sqrt']+[4, 5, 6, '*', 'x^2']+[1, 2, 3, '-', '1/x']+[0, '.', '±', '+', '=']
        btn_tooltips = ['Mod', 'Round', 'Clear', 'Clear all', 'Delete', 'Division', 'Square root', 'Multiply', 'Power', 'Subtract', 'Inverse', 'Decimal separator', 'Negate', 'Add', '']

        css_file_path = os.path.join(os.path.dirname(os.path.relpath(__file__, os.getcwd())), r'style\button.css')
        css_file = open(css_file_path)
        btn_css_code = css_file.read()
        css_file.close()

        tooltips_idx = 0
        for i in btn_texts:
            btn = CalculatorPadBtnPushButton(str(i))
            btn.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
            btn.setStyleSheet(btn_css_code)

            if isinstance(i, int):
                pass
            else:
                btn.setToolTip(btn_tooltips[tooltips_idx])
                tooltips_idx += 1

            self.__number_btns.append(btn)

        gridLayout = QGridLayout()
        for i in range(len(self.__number_btns)):
            gridLayout.addWidget(self.__number_btns[i], i // 5, i % 5)

        gridLayout.setSpacing(0)
        gridLayout.setContentsMargins(2, 2, 2, 2)
        self.setLayout(gridLayout)

    def getBtns(self):
        return self.__number_btns