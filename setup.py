from setuptools import setup, find_packages

setup(
    name='pyqt-dark-calculator',
    version='0.1.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_dark_calculator.ico': ['calculator.svg'],
                  'pyqt_dark_calculator.style': ['calculator_pad_button.css']},
    description='PyQt5 dark calculator',
    url='https://github.com/yjg30737/pyqt-dark-calculator.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-dark-gray-theme @ git+https://git@github.com/yjg30737/pyqt-dark-gray-theme.git@main',
        'pyqt-custom-titlebar-window @ git+https://git@github.com/yjg30737/pyqt-custom-titlebar-window.git@main',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main'
    ]
)