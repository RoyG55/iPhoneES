from PyQt6.QtWidgets import QHBoxLayout, QPushButton, QCheckBox
from prot_Win_st_2 import *
from main_Win_st_3 import NewWindow29
class NewNewWindow4(QDialog):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,200,300)
        self.setWindowTitle("iCPU-Fix ExpSys")
        self.formulario()
        self.show()

    def formulario(self):

        self.label = QLabel("Paso 2: Revisa las siguientes lineas por cortos o fugas, marca cada casilla si pasaron la prueba")
        self.option1 = QCheckBox("PP_CPU_PCORE")
        self.option2 = QCheckBox("PP_GPU")
        self.option3 = QCheckBox("PP_SOC_S1")
        self.option4 = QCheckBox("PP1V8_S4")
        self.option5 = QCheckBox("PP1V06_S2")
        self.option6 = QCheckBox("PP_AVE_S1")
        self.option7 = QCheckBox("PP1V2_S4")
        self.option8 = QCheckBox("PP_SRAM_S1")
        self.option9 = QCheckBox("PP_DISP_S1")
        self.option10 = QCheckBox("PP1VX_DISPLAY_S2")
        self.option11 = QCheckBox("PP_CPU_SRAM")
        self.option12 = QCheckBox("PP_CPU_ECORE")
        self.option13 = QCheckBox("P0V9_S1")
        self.option14 = QCheckBox("PP_DCS_S1")
        self.option15 = QCheckBox("PP3V3_USB_S2")
        self.option16 = QCheckBox("PP1V8_AUDIO_VA_S2")
        self.option17 = QCheckBox("PP1V2_SOC")
        self.option18 = QCheckBox("PP0V7_VDD_LOW_S2")
        self.option19 = QCheckBox("PP2V625_NAND")
        self.option20 = QCheckBox("PP1V2_NFC_S2")
        self.option21 = QCheckBox("PP3V0_S2")
        self.option22 = QCheckBox("PP1V0_S4")
        self.option23 = QCheckBox("PP1V8_ALWAYS")
        self.option24 = QCheckBox("PP3V0_DISPLAY_S2")
        self.option25 = QCheckBox("PP0V6_VDDOL_S1")
        self.option26 = QCheckBox("PP0V78_SOC_FIXED_S1")
        self.option27 = QCheckBox("PPVAR_EIGER_S2")
        self.option28 = QCheckBox("PP1V5_VLDOINT")
        self.option29 = QCheckBox("No encontré ningun corto")
        self.mensaje = QLabel("")
        self.next_button = QPushButton("Siguiente")
        self.next_button.clicked.connect(self.open_new_window)


        vertical_layout1 = QVBoxLayout()

        h_layout_1 = QHBoxLayout()
        h_layout_2 = QHBoxLayout()
        h_layout_3 = QHBoxLayout()
        h_layout_4 = QHBoxLayout()
        h_layout_5 = QHBoxLayout()
        h_layout_6 = QHBoxLayout()
        h_layout_7 = QHBoxLayout()
        h_layout_8 = QHBoxLayout()
        h_layout_9 = QHBoxLayout()
        h_layout_10 = QHBoxLayout()
        h_layout_11 = QHBoxLayout()
        h_layout_12 = QHBoxLayout()
        h_layout_13 = QHBoxLayout()
        h_layout_14 = QHBoxLayout()

        h_layout_1.addWidget(self.option1)
        h_layout_1.addWidget(self.option15)

        h_layout_2.addWidget(self.option2)
        h_layout_2.addWidget(self.option16)

        h_layout_3.addWidget(self.option3)
        h_layout_3.addWidget(self.option17)

        h_layout_4.addWidget(self.option4)
        h_layout_4.addWidget(self.option18)

        h_layout_5.addWidget(self.option5)
        h_layout_5.addWidget(self.option19)

        h_layout_6.addWidget(self.option6)
        h_layout_6.addWidget(self.option20)

        h_layout_7.addWidget(self.option7)
        h_layout_7.addWidget(self.option21)

        h_layout_8.addWidget(self.option8)
        h_layout_8.addWidget(self.option22)

        h_layout_9.addWidget(self.option9)
        h_layout_9.addWidget(self.option23)

        h_layout_10.addWidget(self.option10)
        h_layout_10.addWidget(self.option24)

        h_layout_11.addWidget(self.option11)
        h_layout_11.addWidget(self.option25)

        h_layout_12.addWidget(self.option12)
        h_layout_12.addWidget(self.option26)

        h_layout_13.addWidget(self.option13)
        h_layout_13.addWidget(self.option27)

        h_layout_14.addWidget(self.option14)
        h_layout_14.addWidget(self.option28)




        vertical_layout1.addWidget(self.label)
        vertical_layout1.addLayout(h_layout_1)
        vertical_layout1.addLayout(h_layout_2)
        vertical_layout1.addLayout(h_layout_3)
        vertical_layout1.addLayout(h_layout_4)
        vertical_layout1.addLayout(h_layout_5)
        vertical_layout1.addLayout(h_layout_6)
        vertical_layout1.addLayout(h_layout_7)
        vertical_layout1.addLayout(h_layout_8)
        vertical_layout1.addLayout(h_layout_9)
        vertical_layout1.addLayout(h_layout_10)
        vertical_layout1.addLayout(h_layout_11)
        vertical_layout1.addLayout(h_layout_12)
        vertical_layout1.addLayout(h_layout_13)
        vertical_layout1.addLayout(h_layout_14)
        vertical_layout1.addWidget(self.option29)
        vertical_layout1.addWidget(self.mensaje)
        vertical_layout1.addWidget(self.next_button)

        self.setLayout(vertical_layout1)

    def open_new_window(self):
        if self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option1.isChecked() and not self.option29.isChecked():
            new_window = NewWindow1()
            new_window.exec()
        elif self.option1.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option2.isChecked() and not self.option29.isChecked():
            new_window = NewWindow2()
            new_window.exec()
        elif self.option2.isChecked() and self.option1.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option3.isChecked() and not self.option29.isChecked():
            new_window = NewWindow3()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option1.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option4.isChecked() and not self.option29.isChecked():
            new_window = NewWindow4()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option1.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option5.isChecked() and not self.option29.isChecked():
            new_window = NewWindow5()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option1.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option6.isChecked() and not self.option29.isChecked():
            new_window = NewWindow6()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option1.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option7.isChecked() and not self.option29.isChecked():
            new_window = NewWindow7()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option1.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option8.isChecked() and not self.option29.isChecked():
            new_window = NewWindow8()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option1.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option9.isChecked() and not self.option29.isChecked():
            new_window = NewWindow9()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option1.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option10.isChecked() and not self.option29.isChecked():
            new_window = NewWindow10()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option1.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option11.isChecked() and not self.option29.isChecked():
            new_window = NewWindow11()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option1.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option12.isChecked() and not self.option29.isChecked():
            new_window = NewWindow12()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option1.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option13.isChecked() and not self.option29.isChecked():
            new_window = NewWindow13()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option1.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option14.isChecked() and not self.option29.isChecked():
            new_window = NewWindow14()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option1.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option15.isChecked() and not self.option29.isChecked():
            new_window = NewWindow15()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option1.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option16.isChecked() and not self.option29.isChecked():
            new_window = NewWindow16()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option1.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option17.isChecked() and not self.option29.isChecked():
            new_window = NewWindow17()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option1.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option18.isChecked() and not self.option29.isChecked():
            new_window = NewWindow18()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option1.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option19.isChecked() and not self.option29.isChecked():
            new_window = NewWindow19()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option1.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option20.isChecked() and not self.option29.isChecked():
            new_window = NewWindow20()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option1.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option21.isChecked() and not self.option29.isChecked():
            new_window = NewWindow21()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option1.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option22.isChecked() and not self.option29.isChecked():
            new_window = NewWindow22()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option1.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option23.isChecked() and not self.option29.isChecked():
            new_window = NewWindow23()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option1.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option24.isChecked() and not self.option29.isChecked():
            new_window = NewWindow24()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option1.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option25.isChecked() and not self.option29.isChecked():
            new_window = NewWindow25()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option1.isChecked() and self.option27.isChecked() and self.option28.isChecked() and not self.option26.isChecked() and not self.option29.isChecked():
            new_window = NewWindow26()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option1.isChecked() and self.option28.isChecked() and not self.option27.isChecked() and not self.option29.isChecked():
            new_window = NewWindow27()
            new_window.exec()
        elif self.option2.isChecked() and self.option3.isChecked() and self.option4.isChecked() and self.option5.isChecked() and self.option6.isChecked() and self.option7.isChecked() and self.option8.isChecked() and self.option9.isChecked() and self.option10.isChecked()  and self.option11.isChecked() and self.option12.isChecked() and self.option13.isChecked() and self.option14.isChecked() and self.option15.isChecked() and self.option16.isChecked() and self.option17.isChecked() and self.option18.isChecked() and self.option19.isChecked() and self.option20.isChecked() and self.option21.isChecked() and self.option22.isChecked() and self.option23.isChecked() and self.option24.isChecked() and self.option25.isChecked() and self.option26.isChecked() and self.option27.isChecked() and self.option1.isChecked() and not self.option28.isChecked() and not self.option29.isChecked():
            new_window = NewWindow28()
            new_window.exec()
        elif self.option29.isChecked() and not self.option3.isChecked() and not self.option4.isChecked() and not self.option5.isChecked() and not self.option6.isChecked() and not self.option7.isChecked() and not self.option8.isChecked() and not self.option9.isChecked() and not self.option10.isChecked()  and not self.option11.isChecked() and not self.option12.isChecked() and not self.option13.isChecked() and not self.option14.isChecked() and not self.option15.isChecked() and not self.option16.isChecked() and not self.option17.isChecked() and not self.option18.isChecked() and not self.option19.isChecked() and not self.option20.isChecked() and not self.option21.isChecked() and not self.option22.isChecked() and not self.option23.isChecked() and not self.option24.isChecked() and not self.option25.isChecked() and not self.option26.isChecked() and not self.option27.isChecked() and not self.option28.isChecked() and not self.option1.isChecked() and not self.option2.isChecked():
            self.close()
            new_window = NewWindow29()
            new_window.exec()
        else:
            self.mensaje.setText(f"No ingresaste una opcion valida")
