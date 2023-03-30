from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # перевірка типів значень, що вводяться
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout, QGridLayout,
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
 
from instr import *
from second_win import *


class MainWin(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.set_appear()
        self.show()
    
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)


    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.instruction, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.button)
        self.connects()

        return self.layout
    
    def next_click(self):
        self.tw = TestWin()
        self.hide()

    
    def connects(self):
        self.button.clicked.connect(self.next_click)


app = QApplication([])
mw = MainWin()
mw.setLayout(mw.initUI())
app.exec_()