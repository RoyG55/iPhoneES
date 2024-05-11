import sys
from PyQt6.QtWidgets import (QApplication, QWidget,QMessageBox, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QComboBox, QDialog)
from mainWin import NewWindow
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QDate

class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.iniUI()

    def iniUI(self):
        self.setMinimumHeight(300)
        self.setMinimumWidth(300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        welcome_mesage = QLabel("Analizador de fallas de encendido")
        welcome_mesage.setFont(QFont("Arial",20))
        welcome_mesage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        select_model_label = QLabel('Selecciona el modelo:')
        select_model_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        iphone12_boton = QPushButton("iPhone 12")
        iphone12_boton.clicked.connect(self.open_new_window)
        iPhone12_Pro_boton = QPushButton("iPhone 12 Pro")

        layout = QVBoxLayout()
        layout.addWidget(welcome_mesage,-700)
        layout.addWidget(select_model_label)
        layout.addWidget(iphone12_boton)
        layout.addWidget(iPhone12_Pro_boton)

        self.setLayout(layout)


    def open_new_window(self):
        self.close()
        new_window = NewWindow()
        new_window.exec()











if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = mainWindow()
    sys.exit(app.exec())