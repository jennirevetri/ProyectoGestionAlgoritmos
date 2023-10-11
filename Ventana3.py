from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
from gestionFacturas import *

class Ventana3:

    

    def __init__(self,ventana2):
        self.ventana2 = ventana2
        self.ventana2.geometry("900x500")
        self.ventana2.configure(background = "white")

        self.fuente_consolas_grande = tkFont.Font(family="Consolas", size=20)
        self.fuente_consolas_pequeño = tkFont.Font(family="Consolas", size=14)
        self.fuentePequeña = tkFont.Font(family="Consolas", size=10)

        self.set_widgets()
        self.cargar_datos()
        

    def set_widgets(self):
        tituloVentana2 = Label(self.ventana2, text="MODULO DE FACTURACION",bg="#CACACA",fg="#0F1B0D",font=self.fuente_consolas_grande)
        tituloVentana2.place(x=0,y=0,width=900,height=70)
        frame = LabelFrame(self.ventana2,bg="#899B87")
        frame.place(x=0,y=70,width=150,height=430)

        self.boton1 = Button(frame,text="CREAR",font=self.fuentePequeña,width=10,height=2,bg="#0F1B0D",fg="#CACACA",command=self.crear_factura)
        self.boton1.place(x=35,y=80)
        self.boton2 = Button(frame,text="ELIMINAR",font=self.fuentePequeña,width=10,height=2,bg="#0F1B0D",fg="#CACACA",command= self.elimina_factura)
        self.boton2.place(x=35,y=180)
        self.boton3 = Button(frame,text="MODIFICAR",font=self.fuentePequeña,width=10,height=2,bg="#0F1B0D",fg="#CACACA",command=self.modifica_factura)
        self.boton3.place(x=35,y=280)

        frame2 = LabelFrame(self.ventana2,bg="#ADC4AB")
        frame2.place(x=152,y=70,width=205,height=430)
        label1= Label(frame2,text="ID Factura: ",bg="#ADC4AB",font=self.fuente_consolas_pequeño,fg="#0F1B0D")
        label1.place(x=10,y=10)
        self.entrada1= Entry(frame2,bg="#CACACA",font=self.fuente_consolas_pequeño,fg="#0F1B0D",width=15)
        self.entrada1.place(x=10,y=40)
        label2= Label(frame2,text="Costo Total: ",bg="#ADC4AB",font=self.fuente_consolas_pequeño,fg="#0F1B0D")
        label2.place(x=10,y=80)
        self.entrada2= Entry(frame2,bg="#CACACA",font=self.fuente_consolas_pequeño,fg="#0F1B0D",width=15)
        self.entrada2.place(x=10,y=110)
        label3= Label(frame2,text="Servicios: ",bg="#ADC4AB",font=self.fuente_consolas_pequeño,fg="#0F1B0D")
        label3.place(x=10,y=150)
        self.entrada3= Entry(frame2,bg="#CACACA",font=self.fuente_consolas_pequeño,fg="#0F1B0D",width=15)
        self.entrada3.place(x=10,y=180)
        label4= Label(frame2,text="Metodo de pago: ",bg="#ADC4AB",font=self.fuente_consolas_pequeño,fg="#0F1B0D")
        label4.place(x=10,y=220)
        self.entrada4= Entry(frame2,bg="#CACACA",font=self.fuente_consolas_pequeño,fg="#0F1B0D",width=15)
        self.entrada4.place(x=10,y=250)
        label5= Label(frame2,text="Estado de Pago: ",bg="#ADC4AB",font=self.fuente_consolas_pequeño,fg="#0F1B0D")
        label5.place(x=10,y=290)
        self.entrada5= Entry(frame2,bg="#CACACA",font=self.fuente_consolas_pequeño,fg="#0F1B0D",width=15)
        self.entrada5.place(x=10,y=320)

        
        

        self.grid = ttk.Treeview(self.ventana2,columns=('ID_Factura', 'Costo_Total', 'Servicios', 'Metodo_Pago', 'Estado_Pago'))
        self.grid.heading('#1', text='ID_Factura')
        self.grid.heading('#2', text='Costo_Total')
        self.grid.heading('#3', text='Servicios')
        self.grid.heading('#4', text='Metodo_Pago')
        self.grid.heading('#5', text='Estado_Pago')
        self.grid.column("#0", width=0)

        # Establecer el ancho de las columnas
        self.grid.column("#1", width=90)
        self.grid.column("#2", width=90)
        self.grid.column("#3", width=90)
        self.grid.column("#4", width=90)
        self.grid.column("#5", width=90)
        
        # Alinear las columnas al centro
        self.grid.column("#1", anchor="center")
        self.grid.column("#2", anchor="center")
        self.grid.column("#3", anchor="center")
        self.grid.column("#4", anchor="center")
        self.grid.column("#5", anchor="center")
        self.grid.place(x=355,y=70,width=550,height=500)
        


    def cargar_datos(self):
    # Borrar todos los elementos del TreeView
        self.grid.delete(*self.grid.get_children())
        
        # Cargar los datos desde el archivo CSV al iniciar la aplicación
        facturas = cargar_facturas()

        # Actualizar el TreeView con los datos cargados
        self.actualizar_tabla(facturas)

    def actualizar_tabla(self, facturas):
    # Borra todos los elementos de la tabla
        self.grid.delete(*self.grid.get_children())

        # Llena la tabla con los datos actualizados
        for factura in facturas:
            self.grid.insert('', 'end', values=(factura.id_factura, factura.costo_total, factura.servicios, factura.metodo_pago, factura.estado_pago))


    def crear_factura(self):
    # Obtener los valores de las entradas
        id_factura = int(self.entrada1.get())
        costo_total = float(self.entrada2.get())
        servicios = self.entrada3.get()
        metodo_pago = self.entrada4.get()
        estado_pago = self.entrada5.get()

        # Llamar a la función para crear una factura
        insertar_factura(id_factura, costo_total, servicios, metodo_pago, estado_pago)

        # Recargar los datos desde el archivo CSV
        facturas = cargar_facturas()

        # Actualizar la tabla con los datos cargados
        self.actualizar_tabla(facturas)

    def elimina_factura(self):
        # Obtener el valor de la entrada
        id_factura = int(self.entrada1.get())

        # Llamar a la función para eliminar una factura
        eliminar_factura(id_factura)

        # Recargar los datos desde el archivo CSV
        facturas = cargar_facturas()

        # Actualizar la tabla con los datos cargados
        self.actualizar_tabla(facturas)

    def modifica_factura(self):
        # Obtener los valores de las entradas
        id_factura = int(self.entrada1.get())
        costo_total = float(self.entrada2.get())
        servicios = self.entrada3.get()
        metodo_pago = self.entrada4.get()
        estado_pago = self.entrada5.get()

        # Llamar a la función para modificar una factura
        modificar_factura(id_factura, costo_total, servicios, metodo_pago, estado_pago)

        # Recargar los datos desde el archivo CSV
        facturas = cargar_facturas()

        # Actualizar la tabla con los datos cargados
        self.actualizar_tabla(facturas)


    

    def limpiar_entradas(self):
    # Borra el contenido de todas las entradas
        self.entrada1.delete(0, "end")
        self.entrada2.delete(0, "end")
        self.entrada3.delete(0, "end")
        self.entrada4.delete(0, "end")
        self.entrada5.delete(0, "end")