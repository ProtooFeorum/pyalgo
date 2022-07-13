from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *
from final_win import *

class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
#       <-----Создание окна----->        
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
#       <-----Виджеты----->        
    def initUI(self):
        self.name = QLabel(txt_name)
        self.line_name = QLineEdit(txt_hintname)
        self.age = QLabel(txt_age)
        self.line_age = QLineEdit(txt_hintage)
        self.test1 = QLabel(txt_test1)
        self.test1_button = QPushButton(txt_starttest1) 
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.test2 = QLabel(txt_test2)
        self.test2_button = QPushButton(txt_starttest2) 
        self.test3 = QLabel(txt_test3)
        self.test3_button = QPushButton(txt_starttest3) 
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)
        self.sendresults = QPushButton(txt_sendresults)
        self.h_line = QHBoxLayout()
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
#       <-----Отображение виджетов----->
        self.l_line.addWidget(self.name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test1_button, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test2_button, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test3_button, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.sendresults, alignment = Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
#       <-----Реакция на нажатие кнопки----->        
    def connects(self):
        self.sendresults.clicked.connect(self.next_click2)
    def next_click2(self):
        self.hide()
        self.fw = FinalWin()    