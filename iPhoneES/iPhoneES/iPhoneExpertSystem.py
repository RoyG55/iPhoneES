class iPhoneExpertSystem:
    def __init__(self):

        self.rules = {
            "Consumo total inicial en fuente de poder": ["Corto en linea PP_BATT_VCC_YANGTZE",
                                                         "Corto en linea PP_VDD_MAIN",
                                                         "Corto en linea PP_VDD_BOOST"],
            "Consumo total en fuente de poder despues de presionar el boton de power": ["Corto en linea PP_CPU_PCORE",
                                                                                       "Corto en linea PP_GPU",
                                                                                       "Corto en linea PP_SOC_S1",
                                                                                       "Corto en linea PP1V8_S4",
                                                                                       "Corto en linea PP1V06_S2",
                                                                                       "Corto en linea PP_AVE_S1",
                                                                                       "Corto en linea PP1V2_S4",
                                                                                       "Corto en linea PP_SRAM_S1",
                                                                                       "Corto en linea PP_DISP_S1",
                                                                                       "Corto en linea PP1VX_DISPLAY_S2",
                                                                                       "Corto en linea PP_CPU_SRAM",
                                                                                       "Corto en linea PP_CPU_ECORE",
                                                                                       "Corto en linea P0V9_S1",
                                                                                       "Corto en linea PP_DCS_S1",
                                                                                       "Corto en linea PP3V3_USB_S2",
                                                                                       "Corto en linea PP1V8_AUDIO_VA_S2",
                                                                                       "Corto en linea PP1V2_SOC",
                                                                                       "Corto en linea PP0V7_VDD_LOW_S2",
                                                                                       "Corto en linea PP2V625_NAND",
                                                                                       "Corto en linea PP1V2_NFC_S2",
                                                                                       "Corto en linea PP3V0_S2",
                                                                                       "Corto en linea PP1V0_S4",
                                                                                       "Corto en linea PP1V8_ALWAYS",
                                                                                       "Corto en linea PP3V0_DISPLAY_S2",
                                                                                       "Corto en linea PP0V6_VDDOL_S1",
                                                                                       "Corto en linea PP0V78_SOC_FIXED_S1",
                                                                                       "Corto en linea PPVAR_EIGER_S2",
                                                                                       "Corto en linea PP1V5_VLDOINT"],
            "Consumo bajo fijo inicial": ["Bobinas sueltas en la placa",
                                           "Memoria NAND desoldada",
                                           "Memoria NAND sin comunicacion con CPU"]
        }

    def diagnose_issue(self, symptom):
        possible_causes = self.rules.get(symptom)
        if possible_causes:
            return possible_causes
        else:
            return "No se encontraron posibles causas para el síntoma proporcionado."


    def reglas(self):
        if "Consumo total inicial en fuente de poder" and "Corto en linea PP_BATT_VCC_YANGTZE":
            print("Busca cualquier componente de la linea VBATT que este en corto y reemplazalo por uno en buen estado")
        else:
            "Consumo total inicial en fuente de poder" and "Corto en linea PP_VDD_MAIN"
            print("Busca cualquier componente de la linea MAIN que este en corto y reemplazalo por uno en buen estado")
        else:
            return("Busca cualquier componente de la linea BOOST que este en corto y reemplazalo por uno en buen estado")


# Ejemplo de uso
expert_system = iPhoneExpertSystem()
symptom = "Consumo total en fuente de poder despues de presionar el boton de power"
possible_causes = expert_system.diagnose_issue(symptom)
if isinstance(possible_causes, list):
    print(f"Posibles causas de '{symptom}':")
    for cause in possible_causes:
        print(f"- {cause}")
else:
    print(possible_causes)