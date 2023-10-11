from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
import csv


class VentanaEstadisticas:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana_principal.title("Módulo de Estadísticas y Reportes")
        self.ventana_principal.geometry("730x500")
        self.ventana_principal.configure(background = "white")

        self.fuente_consolas_grande = tkFont.Font(family="Consolas", size=20)
        self.fuente_consolas_pequeño = tkFont.Font(family="Consolas", size=14)
        self.fuentePequeña = tkFont.Font(family="Consolas", size=10)

        self.data = []  # Inicializa data como una lista vacía
        self.datos_actuales = self.data

        self.cargar_datos_csv()
        self.crear_widgets()

    def cargar_datos_csv(self):
        self.data = []
        with open('empleados.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.data.append((row['Hotel'], row['Nombre'], row['Posicion'], row['Salario'], row['Fecha de Contratacion']))
        self.datos_actuales = self.data
        
    def crear_widgets(self):
        self.opcion_seleccionada = StringVar()
        hoteles = set(row[0] for row in self.data)
        self.opcion_menu = ttk.Combobox(self.ventana_principal, textvariable=self.opcion_seleccionada, values=list(hoteles))
        self.opcion_menu.place(x=200,y=10)

        boton_limpiar = Button(self.ventana_principal, text="LIMPIAR",font=self.fuentePequeña,width=15,height=2,bg="#0F1B0D",fg="#CACACA", command=self.limpiar_treeview)
        boton_limpiar.place(x=400,y=10)

        self.tree = ttk.Treeview(self.ventana_principal, columns=("Hotel", "Nombre", "Posición", "Salario", "Fecha de Contratación"), show="headings")
        self.tree.heading("Hotel", text="Hotel")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Posición", text="Posición")
        self.tree.heading("Salario", text="Salario")
        self.tree.heading("Fecha de Contratación", text="Fecha de Contratación")

        self.tree.column("#1", width=90)
        self.tree.column("#2", width=90)
        self.tree.column("#3", width=90)
        self.tree.column("#4", width=90)
        self.tree.column("#5", width=90)
        
        # Alinear las columnas al centro
        self.tree.column("#1", anchor="center")
        self.tree.column("#2", anchor="center")
        self.tree.column("#3", anchor="center")
        self.tree.column("#4", anchor="center")
        self.tree.column("#5", anchor="center")
        self.tree.place(x=10,y=60,width=700,height=380)
        

        boton_calcular_cinco_mas_antiguos = Button(self.ventana_principal, text="Cinco Empleados Más Antiguos", font=self.fuentePequeña,width=30,height=2,bg="#0F1B0D",fg="#CACACA",command=self.cinco_empleados_mas_antiguos_por_hotel)
        boton_calcular_cinco_mas_antiguos.place(x=100,y=450)

        boton_ordenar_empleados_preorden = Button(self.ventana_principal, text="Ordenar Empleados (Preorden)",font=self.fuentePequeña,width=30,height=2,bg="#0F1B0D",fg="#CACACA", command=self.ordenar_empleados_preorden)
        boton_ordenar_empleados_preorden.place(x=350,y=450)

    def cargar_datos_en_treeview(self, datos):
        self.tree.delete(*self.tree.get_children())
        for row in datos:
            self.tree.insert("", "end", values=row)

    def recorrido_inorden_cinco_mas_antiguos(self, raiz, result=[]):
        if raiz is not None:
            result = self.recorrido_inorden_cinco_mas_antiguos(raiz.izquierda, result)
            result.append(raiz.empleado)
            if len(result) == 5:
                return result
            result = self.recorrido_inorden_cinco_mas_antiguos(raiz.derecha, result)
        return result
    
    def limpiar_treeview(self):
        self.tree.delete(*self.tree.get_children())



    def recorrido_preorden(self, raiz, result=[]):
        if raiz is not None:
            result.append(raiz.empleado)
            result = self.recorrido_preorden(raiz.izquierda, result)
            result = self.recorrido_preorden(raiz.derecha, result)
        return result


    def cinco_empleados_mas_antiguos_por_hotel(self):
        self.limpiar_treeview()
        self.datos_actuales = []  # Limpia los datos actuales
        

        hotel_seleccionado = self.opcion_seleccionada.get()
        empleados_hotel = [row for row in self.data if row[0] == hotel_seleccionado]

        if empleados_hotel:
            class Nodo:
                def __init__(self, empleado):
                    self.empleado = empleado
                    self.izquierda = None
                    self.derecha = None

            raiz = None
            for empleado in empleados_hotel:
                fecha_contratacion = empleado[4]
                nuevo_nodo = Nodo(empleado)
                if raiz is None:
                    raiz = nuevo_nodo
                else:
                    actual = raiz
                    while True:
                        if fecha_contratacion < actual.empleado[4]:
                            if actual.izquierda is None:
                                actual.izquierda = nuevo_nodo
                                break
                            actual = actual.izquierda
                        else:
                            if actual.derecha is None:
                                actual.derecha = nuevo_nodo
                                break
                            actual = actual.derecha

            cinco_mas_antiguos = self.recorrido_inorden_cinco_mas_antiguos(raiz)
            self.datos_actuales = cinco_mas_antiguos  # Actualiza self.datos_actuales
            self.cargar_datos_en_treeview(cinco_mas_antiguos)

    def ordenar_empleados_preorden(self):
        self.limpiar_treeview()
        self.datos_actuales = []  # Limpia los datos actuales
        

        hotel_seleccionado = self.opcion_seleccionada.get()
        empleados_hotel = [row for row in self.data if row[0] == hotel_seleccionado]

        if empleados_hotel:
            class Nodo:
                def __init__(self, empleado):
                    self.empleado = empleado
                    self.izquierda = None
                    self.derecha = None

            raiz = None
            for empleado in empleados_hotel:
                fecha_contratacion = empleado[4]
                nuevo_nodo = Nodo(empleado)
                if raiz is None:
                    raiz = nuevo_nodo
                else:
                    actual = raiz
                    while True:
                        if fecha_contratacion < actual.empleado[4]:
                            if actual.izquierda is None:
                                actual.izquierda = nuevo_nodo
                                break
                            actual = actual.izquierda
                        else:
                            if actual.derecha is None:
                                actual.derecha = nuevo_nodo
                                break
                            actual = actual.derecha

            empleados_ordenados = self.recorrido_preorden(raiz)
            self.datos_actuales = empleados_ordenados  # Actualiza self.datos_actuales
            self.cargar_datos_en_treeview(empleados_ordenados)
