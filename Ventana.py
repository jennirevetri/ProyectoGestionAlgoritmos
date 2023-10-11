from tkinter import *
import tkinter.font as tkFont
from Ventana2 import *
from Ventana3 import *
from gestionEstadisticas import *

class Ventana:

    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.title("Sistema de Gestion")
        self.ventana.geometry("700x500")
        self.ventana.configure(background = "#ADC4AB")

        self.fuente_consolas_grande = tkFont.Font(family="Consolas", size=20)
        self.fuente_consolas_pequeño = tkFont.Font(family="Consolas", size=16)
        self.fuentePequeña = tkFont.Font(family="Consolas", size=10)
        
        self.set_widgets()
        
    

    def set_widgets(self):
        title = Label(self.ventana,text="SISTEMA DE GESTIÓN",width="300",height="2",bg="#CACACA",fg="#0F1B0D",font=self.fuente_consolas_grande).pack()
        boton1 = Button(self.ventana,text="Gestión de Empleados",width=40,height=2,bg="#0F1B0D",fg="#CACACA",font=self.fuente_consolas_pequeño,command =self.ventana_gestion).pack(pady=20)
        boton2 = Button(self.ventana,text="Modulo de Facturacion y Pagos",width=40,height=2,bg="#0F1B0D",fg="#CACACA",font=self.fuente_consolas_pequeño,command=self.ventana_facturas).pack(pady=10)
        boton3 = Button(self.ventana,text="Modulo de Estadisticas y Reportes",width=40,height=2,bg="#0F1B0D",fg="#CACACA",font=self.fuente_consolas_pequeño,command=self.ventana_estadisticas).pack(pady=20)
        
    def ventana_gestion(self):
        employee_tree = EmployeeTree()
        ventana_secundaria = Toplevel(self.ventana)
        ventana = Ventana2(ventana_secundaria, employee_tree)
        ventana_secundaria.title("Gestion de Empleados")
        ventana.set_widgets()
        ventana.cargar_empleados_desde_csv()


    def ventana_facturas(self):
        ventana_tres= Toplevel(self.ventana)
        ventana = Ventana3(ventana_tres)
        ventana_tres.title("Modulo de Facturacion")
        
    def ventana_estadisticas(self):
        ventana_cuatro = Toplevel(self.ventana)
        ventana= VentanaEstadisticas(ventana_cuatro)
        ventana_cuatro.title("Modulo de Estadisticas")
        pass
