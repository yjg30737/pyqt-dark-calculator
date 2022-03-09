from setuptools import setup, find_packages

setup(
    name='pyqt-dark-calculator',
    version='0.6.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_dark_calculator.ico': ['calculator.svg'],
                  'pyqt_dark_calculator.style': ['calculator_pad_button.css']},
    description='PyQt Dark Calculator',
    url='https://github.com/yjg30737/pyqt-dark-calculator.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-style-setter @ git+https://git@github.com/yjg30737/pyqt-style-setter.git@main',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main',
        'python-get-absolute-resource-path @ git+https://git@github.com/yjg30737/python-get-absolute-resource-path.git@main',
        'pyqt-new-window-handler @ git+https://git@github.com/yjg30737/pyqt-new-window-handler.git@main'
    ]
)