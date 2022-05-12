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
    description='PyQt dark calculator',
    url='https://github.com/yjg30737/pyqt-dark-calculator.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-style-setter>=0.0.1',
        'pyqt-resource-helper>=0.0.1',
        'python-get-absolute-resource-path>=0.0.1',
        'pyqt-new-window-handler @ git+https://git@github.com/yjg30737/pyqt-new-window-handler.git@main'
    ]
)