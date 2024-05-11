import sys
from PyQt6.QtWidgets import QButtonGroup, QRadioButton, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QDialog, QLabel, QWidget, QCheckBox

class NewNewWindow4(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,500,300)
        self.setWindowTitle("iCPU-Fix ExpSys")

        layout = QVBoxLayout()

        self.setLayout(layout)