import os.path
from PyQt6.QtWidgets import QVBoxLayout,QDialog, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class NewNewWindow1(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,500,300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        #Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP_BATT_VCC_YANGTZE")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #Indicacion principal
        self.mensaje = QLabel("Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "iPhoneES", "PP_VBATT.png")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()


        vertical_layout = QVBoxLayout()


        #Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)


        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


