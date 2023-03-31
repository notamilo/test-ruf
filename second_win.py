# напиши здесь код для второго экрана приложения

from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

from my_app import * 
from instr import *
from final_win import *

class Experiment():
    def __init__(self, age, input_res, pulse1, pulse2):
        self.age = age
        self.input_res = input_res
        self.pulse1 = pulse1
        self.pulse2 = pulse2
        
    
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)


    def initUI(self):
        self.validator = QIntValidator()
        self.name = QLabel(txt_name) #введіть піб
        self.input_name = QLineEdit(txt_hintname) #П.І.Б.
        
        self.age = QLabel(txt_age) #Повних років
        self.input_age = QLineEdit(txt_hintage) #0
        self.input_age.setValidator(self.validator)

        self.instruction = QLabel(txt_test1) #Ляжте на спину...
        self.button_test = QPushButton(txt_starttest1) #Почати перший тест
        self.input_res = QLineEdit(txt_hinttest1) #0
        self.input_res.setValidator(self.validator)
        
        self.sit_ups = QLabel(txt_test2) #Виконайте 30 присідань
        self.button_test2 = QPushButton(txt_starttest2) #Почати робити присідання

        self.pulse = QLabel(txt_test3) #Ляжте на спину...
        self.button_test3 = QPushButton(txt_starttest3) #Почати фінальний тест
        self.pulse1 = QLineEdit(txt_hinttest2) #0
        self.pulse1.setValidator(self.validator)
        self.pulse2 = QLineEdit(txt_hinttest3) #0
        self.pulse2.setValidator(self.validator)
        
        self.text_timer = QLabel(text_timer) #00:00:00
        self.button_center = QPushButton(txt_finalwin) #Надіслати результати
    
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout() 

        self.l_line.addWidget(self.name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.input_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.input_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_test, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.input_res, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.sit_ups, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.pulse, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.pulse1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.pulse2, alignment = Qt.AlignLeft)

        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignRight)
        self.l_line.addWidget(self.button_center, alignment = Qt.AlignCenter)
        
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    


    def first_timer(self):
        global time
        time = QTime(0, 0, 16)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    
    def timer_sits(self):
        global time
        time = QTime(0, 0, 31)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    
    def timer_final(self):
       global time
       time = QTime(0, 1, 0)
       self.timer = QTimer()
       self.timer.timeout.connect(self.timer3Event)
       self.timer.start(1000)
     
     
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
           self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
           self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
           self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
           self.timer.stop()

    def next_click(self):
        self.hide()
        self.exp = Experiment(int(self.input_age.text()), self.input_res.text(), self.pulse1.text(), self.pulse2.text())
        self.tw = FinalWin(self.exp)
    

    def connects(self):
        self.button_center.clicked.connect(self.next_click)
        self.button_test.clicked.connect(self.first_timer)
        self.button_test2.clicked.connect(self.timer_sits)
        self.button_test3.clicked.connect(self.timer_final)












    
