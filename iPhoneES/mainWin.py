import sys
from PyQt6.QtWidgets import QButtonGroup, QRadioButton, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QDialog, QLabel, QWidget, QCheckBox
from protWindow import NewNewWindow1
from protWindow2 import NewNewWindow2
from protWindow3 import NewNewWindow3
from portWindow4 import NewNewWindow4

class NewWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,200,300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):

        self.label = QLabel("Paso 1: Revisa las siguientes lineas por cortos o fugas, marca cada casilla si pasaron la prueba")
        self.option1 = QCheckBox("PP_BATT_VCC_YANGTZE")
        self.option2 = QCheckBox("PP_VDD_MAIN")
        self.option3 = QCheckBox("PP_VDD_BOOST")
        self.mensaje = QLabel("")
        self.next_button = QPushButton("Siguiente")
        self.next_button.clicked.connect(self.open_new_window)


        vertical_layout = QVBoxLayout()
        h_layout_1 = QHBoxLayout()
        h_layout_2 = QHBoxLayout()
        h_layout_3 = QHBoxLayout()
        h_layout_4 = QHBoxLayout()

        h_layout_1.addWidget(self.option1)
        h_layout_2.addWidget(self.option2)
        h_layout_3.addWidget(self.option3)
        h_layout_4.addWidget(self.mensaje)



        vertical_layout.addWidget(self.label)
        vertical_layout.addLayout(h_layout_1)
        vertical_layout.addLayout(h_layout_2)
        vertical_layout.addLayout(h_layout_3)
        vertical_layout.addLayout(h_layout_4)
        vertical_layout.addWidget(self.next_button)

        self.setLayout(vertical_layout)

    def open_new_window(self):
        if self.option2.isChecked() and self.option3.isChecked():
            new_window = NewNewWindow1()
            new_window.exec()
        elif self.option1.isChecked() and self.option3.isChecked():
            new_window = NewNewWindow2()
            new_window.exec()
        elif self.option1.isChecked() and self.option2.isChecked():
            new_window = NewNewWindow3()
            new_window.exec()
        else:
            self.mensaje.setText(f"No ingresaste una opcion valida")

