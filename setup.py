from setuptools import setup, find_packages

setup(
    name='pyqt-dark-calculator',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    data_files=[('style', ['button.css', 'menu.css', 'theme.css'])],
    packages=find_packages(),
    description='Dark theme calculator made with PyQt5',
    url='https://github.com/yjg30737/pyqt-dark-calculator.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)