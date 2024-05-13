from PyQt6.QtWidgets import QHBoxLayout, QPushButton, QCheckBox
from prot_Win_st_1 import *
from main_Win_st_2 import NewNewWindow4

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
        self.option4 = QCheckBox("No encontré ningun corto")
        self.mensaje = QLabel("")
        self.next_button = QPushButton("Siguiente")
        self.next_button.clicked.connect(self.open_new_window)


        vertical_layout = QVBoxLayout()
        h_layout_1 = QHBoxLayout()
        h_layout_2 = QHBoxLayout()
        h_layout_3 = QHBoxLayout()
        h_layout_4 = QHBoxLayout()
        h_layout_5 = QHBoxLayout()

        h_layout_1.addWidget(self.option1)
        h_layout_2.addWidget(self.option2)
        h_layout_3.addWidget(self.option3)
        h_layout_4.addWidget(self.option4)
        h_layout_5.addWidget(self.mensaje)



        vertical_layout.addWidget(self.label)
        vertical_layout.addLayout(h_layout_1)
        vertical_layout.addLayout(h_layout_2)
        vertical_layout.addLayout(h_layout_3)
        vertical_layout.addLayout(h_layout_4)
        vertical_layout.addLayout(h_layout_5)
        vertical_layout.addWidget(self.next_button)

        self.setLayout(vertical_layout)


    def open_new_window(self):
        if self.option2.isChecked() and self.option3.isChecked() and not self.option1.isChecked() and not self.option4.isChecked():
            new_window = NewNewWindow1()
            new_window.exec()
        elif self.option1.isChecked() and self.option3.isChecked() and not self.option2.isChecked() and not self.option4.isChecked():
            new_window = NewNewWindow2()
            new_window.exec()
        elif self.option1.isChecked() and self.option2.isChecked() and not self.option3.isChecked() and not self.option4.isChecked():
            new_window = NewNewWindow3()
            new_window.exec()
        elif self.option4.isChecked() and not self.option1.isChecked() and not self.option2.isChecked() and not self.option3.isChecked():
            self.close()
            new_window = NewNewWindow4()
            new_window.exec()
        else:
            self.mensaje.setText(f"No ingresaste una opcion valida")

