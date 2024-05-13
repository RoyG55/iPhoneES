from PyQt6.QtWidgets import QHBoxLayout, QPushButton, QCheckBox, QDialog, QLabel, QVBoxLayout
from prot_Win_st_3 import *

class NewWindow29(QDialog):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,200,300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):

        self.label = QLabel("Paso 3: Revisa si hay bobinas sueltas en la placa, de no ser así, revisa las lineas del protocolo PCIE")
        self.label2 = QLabel("Las lineas del protocolo PCIE comunican al CPU con la memoria NAND y solo pasan por 4 condensadores de acoplo.")
        self.label3 = QLabel("Revisa que los condensadores tengan un valor similar de entre 250mV - 600mV en escala de diodo inversa en cada lado.")
        self.label4 = QLabel("Selecciona las casillas si las lineas pasan la prueba")
        self.option1 = QCheckBox("pcie_nand1")
        self.option2 = QCheckBox("pcie_nand2")
        self.option3 = QCheckBox("pcie_nand3")
        self.option4 = QCheckBox("pcie_nand4")
        self.option5 = QCheckBox("pcie_cpu1")
        self.option6 = QCheckBox("pcie_cpu2")
        self.option7 = QCheckBox("pcie_cpu3")
        self.option8 = QCheckBox("pcie_cpu4")
        self.option9 = QCheckBox("todas ok")
        self.mensaje = QLabel("")
        self.next_button = QPushButton("Siguiente")



        vertical_layout = QVBoxLayout()
        h_layout_1 = QHBoxLayout()
        h_layout_2 = QHBoxLayout()
        h_layout_3 = QHBoxLayout()
        h_layout_4 = QHBoxLayout()
        h_layout_5 = QHBoxLayout()

        h_layout_1.addWidget(self.option1)
        h_layout_1.addWidget(self.option5)
        h_layout_2.addWidget(self.option2)
        h_layout_2.addWidget(self.option6)
        h_layout_3.addWidget(self.option3)
        h_layout_3.addWidget(self.option7)
        h_layout_4.addWidget(self.option4)
        h_layout_4.addWidget(self.option8)
        h_layout_5.addWidget(self.option9)
        h_layout_5.addWidget(self.mensaje)



        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.label2)
        vertical_layout.addWidget(self.label3)
        vertical_layout.addWidget(self.label4)
        vertical_layout.addLayout(h_layout_1)
        vertical_layout.addLayout(h_layout_2)
        vertical_layout.addLayout(h_layout_3)
        vertical_layout.addLayout(h_layout_4)
        vertical_layout.addLayout(h_layout_5)
        vertical_layout.addWidget(self.next_button)

        self.setLayout(vertical_layout)