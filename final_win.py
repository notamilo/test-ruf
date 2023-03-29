# напиши здесь код третьего экрана приложения

from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)


from instr import *
from second_win import *
from my_app import *




class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.results()
        self.initUI()
        self.show()

    def results(self):
        self.index = (4*(int(self.exp.input_res)+ int(self.exp.pulse1)+ int(self.exp.pulse2)) - 200) / 10
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif 11 <= self.index < 15:
                return txt_res2
            elif 6 <= self.index < 11:
                return txt_res3
            elif 0.5 <= self.index < 6:
                return txt_res4
            elif self.index < 0.5:
                return txt_res5
        
        elif self.exp.age == 13 or self.exp.age == 14:
            if self.index >= 16.5:
                return txt_res1
            elif 12.5 <= self.index < 16.5:
                return txt_res2
            elif 7.5 <= self.index < 12.5:
                return txt_res3
            elif 2 <= self.index < 7.5:
                return txt_res4
            elif self.index < 2:
                return txt_res5
        
        elif self.exp.age == 11 or self.exp.age == 12:
            if self.index >= 18:
                return txt_res1
            elif 14 <= self.index < 18:
               return txt_res2
            elif 9 <= self.index < 14:
                return txt_res3
            elif 3.5 <= self.index < 9:
                return txt_res4
            elif self.index < 3.5:
                return txt_res5
        
        elif self.exp.age == 9 or self.exp.age == 10:
            if self.index >= 19.5:
                return txt_res1
            elif 15.5 <= self.index < 19.5:
               return txt_res2
            elif 10.5 <= self.index < 15.5:
                return txt_res3
            elif 5 <= self.index < 10.5:
                return txt_res4
            elif self.index < 5:
                return txt_res5

        elif self.exp.age == 7 or self.exp.age == 8:
            if self.index >= 21:
                return txt_res1
            elif 17 <= self.index < 21:
               return txt_res2
            elif 12 <= self.index < 17:
                return txt_res3
            elif 6.5 <= self.index < 12:
                return txt_res4
            elif self.index < 6.5:
                return txt_res5


    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.index_ruf = QLabel(txt_index + str(self.index))
        self.workheart = QLabel(txt_workheart + self.results())
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.index_ruf, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.workheart, alignment = Qt.AlignCenter)
        self.setLayout(self.v_line)
    
    
        










