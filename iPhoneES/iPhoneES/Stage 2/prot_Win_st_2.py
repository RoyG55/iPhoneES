import os.path
from PyQt6.QtWidgets import QVBoxLayout,QDialog, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class NewWindow1(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,500,300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP_CPU_PCORE")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Esta linea es de baja impedancia/resistencia, revisa que el corto sea entre 0.000mV - 0.003mV")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow2(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP_GPU")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Esta linea es de baja impedancia/resistencia, revisa que el corto sea entre 0.000mV - 0.003mV")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow3(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP_SOC_S1")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Esta linea es de baja impedancia/resistencia, revisa que el corto sea entre 0.000mV - 0.003mV")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow4(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP1V8_S4")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel("Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow5(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP1V06_S2")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow6(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP_AVE_S1")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow7(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP1V2_S4")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow8(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP_SRAM_S1")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow9(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP_DISP_S1")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow10(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP1VX_DISPLAY_S2")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow11(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP_CPU_SRAM")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow12(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP_CPU_ECORE")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow13(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP0V9_S1")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow14(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP_DCS_S1")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow15(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP3V3_USB_S2")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow16(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP1V8_AUDIO_VA_S2")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow17(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP1V2_SOC")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow18(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP0V7_VDD_LOW_S2")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow19(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP2V625_NAND")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow20(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP1V2_NFC_S2")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow21(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP3V0_S2")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow22(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP1V0_S4")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow23(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP1V8_ALWAYS")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow24(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP3V0_DISPLAY_S2")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow25(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP0V06_VDDOL_S1")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow26(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP0V78_SOC_FIXED_S1")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow27(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PPVAR_EIGER_S2")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)


class NewWindow28(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):
        # Crea label principal y define tamano y alineacion
        self.label = QLabel("Corto en linea PP1V5_VLDOINT")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Indicacion principal
        self.mensaje = QLabel(
            "Inyecta tension y revisa con camara termica o rosin que componente esta en corto y reemplazalo")
        self.mensaje.setFont(QFont("Arial", 16))
        self.mensaje2 = QLabel("Imagen de referencia:")
        self.mensaje2.setFont(QFont("Arial", 12))
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, "../iPhoneES", "--")
        self.imagen = QPixmap(self.image_path)
        self.imagen_label = QLabel()

        vertical_layout = QVBoxLayout()

        # Agrupacion de los elementos en un vertical Layout

        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.mensaje)
        vertical_layout.addWidget(self.mensaje2)
        vertical_layout.addWidget(self.imagen_label)

        self.setLayout(vertical_layout)
        self.imagen_label.setPixmap(self.imagen)

