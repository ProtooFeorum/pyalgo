from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from instr import *
from second_win import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
#       <-----Создание окна----->        
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
#       <-----Виджеты----->        
    def initUI(self):
        self.index = QLabel(txt_index)
        self.workheart = QLabel(txt_workheart)
        self.main_layout = QVBoxLayout()
#       <-----Отображение виджетов----->
        self.main_layout.addWidget(self.index, alignment = Qt.AlignCenter)
        self.main_layout.addWidget(self.workheart, alignment = Qt.AlignCenter)
        self.setLayout(self.main_layout)
    def connects(self):
        pass    