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
#       <-----Отображение виджетов----->
        self.layout.addWidget(self.hello_text, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.instruction, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.button, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)
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








