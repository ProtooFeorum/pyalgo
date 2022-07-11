from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from instr import *
from second_win import *

class MainWin(QWidget):
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
#       <-----Определение виджетов----->        
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout()
#       <-----Добавление виджетов----->
        self.layout.addWidget(self.hello_text, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.instruction, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.button, alignment = Qt.AlignCenter)
#       <-----Реакция на нажатие на кнопку----->        
    def connects(self):
        self.button.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = SecondWin()    

    
App = QApplication([])
main_win = MainWin()

main_win.show()
App.exec()









# v_line = QVBoxLayout()
# h_line1 = QHBoxLayout()
# h_line2 = QHBoxLayout()
# h_line3 = QHBoxLayout()
# button1 = QPushButton('1')
# button2 = QPushButton('2')
# button3 = QPushButton('3')
# button4 = QPushButton('4')
# button5 = QPushButton('5')

# main_win.setLayout(h_line)
# h_line1.addWidget(button1, alignment = Qt.AlignLeft)
# h_line1.addWidget(button2, alignment = Qt.AlignRight)
# h_line2.addWidget(button3, alignment = Qt.AlignCenter)
# h_line3.addWidget(button4, alignment = Qt.AlignLeft)
# h_line3.addWidget(button5, alignment = Qt.AlignRight)

# v_line.addLayout(h_line1)
# v_line.addLayout(h_line2)
# v_line.addLayout(h_line3)
# main_win.setLayout(v_line)
