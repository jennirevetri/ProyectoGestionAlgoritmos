from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
import csv
from gestionEmpleados import *

from tkinter import messagebox

class Ventana2:

    

    def __init__(self,ventana2,employee_tree):
        self.ventana2 = ventana2
        self.employee_tree = employee_tree
        self.ventana2.geometry("900x500")
        self.ventana2.configure(background = "white")

        self.fuente_consolas_grande = tkFont.Font(family="Consolas", size=20)
        self.fuente_consolas_pequeño = tkFont.Font(family="Consolas", size=14)
        self.fuentePequeña = tkFont.Font(family="Consolas", size=10)
        self.set_widgets()
        
        

        
    def cargar_empleados_desde_csv(self):
        cargar_empleados("empleados.csv", self.employee_tree)
        self.employee_tree.in_order_traversal(self.employee_tree.root, self.grid)


    def crear_empleado(self):
        # Obtener los datos ingresados por el usuario desde self.entrada1, self.entrada2, etc.
        hotel = self.entrada1.get()
        nombre = self.entrada2.get()
        posicion = self.entrada3.get()
        salario = self.entrada4.get()
        fecha_contratacion = self.entrada5.get()
        
        for row in self.grid.get_children():
            self.grid.delete(row)

         # Llamar a la función para insertar el nuevo empleado en el árbol binario
        self.employee_tree.insert(hotel, nombre, posicion, salario, fecha_contratacion)

        self.employee_tree.in_order_traversal(self.employee_tree.root, self.grid)
        
        

        # Limpiar los campos de entrada después de la inserción
        self.entrada1.delete(0, 'end')
        self.entrada2.delete(0, 'end')
        self.entrada3.delete(0, 'end')
        self.entrada4.delete(0, 'end')
        self.entrada5.delete(0, 'end')

    def eliminar_empleado(self):
        # Obtener el item seleccionado en el TreeView
        seleccionado = self.grid.selection()
        if not seleccionado:
            messagebox.showerror("Error", "Por favor, seleccione un empleado para eliminar.")
            return

        
        
        # Obtener el nombre del empleado seleccionado
        item = self.grid.item(seleccionado)
        nombre_empleado = item['values'][1]  # Suponiendo que el nombre está en la segunda columna

        # Eliminar el empleado del árbol binario
        self.employee_tree.eliminar(nombre_empleado)

        # Eliminar el elemento seleccionado del TreeView
        self.grid.delete(seleccionado)

    def modificar_empleado(self):
    # Obtener el item seleccionado en el TreeView
        seleccionado = self.grid.selection()
        if not seleccionado:
            messagebox.showerror("Error", "Por favor, seleccione un empleado para modificar.")
            return

        # Obtener el nombre del empleado seleccionado
        item = self.grid.item(seleccionado) 
        
        nombre = item['values'][1]
        
        # Obtener los nuevos datos ingresados por el usuario
        nuevo_nombre = self.entrada2.get()
        nueva_posicion = self.entrada3.get()
        nuevo_salario = self.entrada4.get()
        nueva_fecha_contratacion = self.entrada5.get()

        # Llamar a una función para modificar el empleado en el árbol binario
        self.employee_tree.modificar(nombre, nuevo_nombre, nueva_posicion, nuevo_salario, nueva_fecha_contratacion)

        # Actualizar el TreeView
        self.actualizar_treeview()

    def actualizar_treeview(self):
        # Limpiar el TreeView
        for row in self.grid.get_children():
            self.grid.delete(row)

        # Llamar a in_order_traversal para mostrar los datos actualizados en el TreeView
        self.employee_tree.in_order_traversal(self.employee_tree.root, self.grid)


    def set_widgets(self):
        tituloVentana2 = Label(self.ventana2, text="GESTION DE EMPLEADOS",bg="#CACACA",fg="#0F1B0D",font=self.fuente_consolas_grande)
        tituloVentana2.place(x=0,y=0,width=900,height=70)
        frame = LabelFrame(self.ventana2,bg="#899B87")
        frame.place(x=0,y=70,width=150,height=430)

        self.boton1 = Button(frame,text="CREAR",font=self.fuentePequeña,width=10,height=2,bg="#0F1B0D",fg="#CACACA",command=self.crear_empleado)
        self.boton1.place(x=35,y=80)
        self.boton2 = Button(frame,text="ELIMINAR",font=self.fuentePequeña,width=10,height=2,bg="#0F1B0D",fg="#CACACA",command=self.eliminar_empleado)
        self.boton2.place(x=35,y=180)
        self.boton3 = Button(frame,text="MODIFICAR",font=self.fuentePequeña,width=10,height=2,bg="#0F1B0D",fg="#CACACA",command=self.modificar_empleado)
        self.boton3.place(x=35,y=280)

        frame2 = LabelFrame(self.ventana2,bg="#ADC4AB")
        frame2.place(x=152,y=70,width=205,height=430)
        label1= Label(frame2,text="Hotel: ",bg="#ADC4AB",font=self.fuente_consolas_pequeño,fg="#0F1B0D")
        label1.place(x=10,y=10)
        self.entrada1= Entry(frame2,bg="#CACACA",font=self.fuente_consolas_pequeño,fg="#0F1B0D",width=15)
        self.entrada1.place(x=10,y=40)
        label2= Label(frame2,text="Nombre: ",bg="#ADC4AB",font=self.fuente_consolas_pequeño,fg="#0F1B0D")
        label2.place(x=10,y=80)
        self.entrada2= Entry(frame2,bg="#CACACA",font=self.fuente_consolas_pequeño,fg="#0F1B0D",width=15)
        self.entrada2.place(x=10,y=110)
        label3= Label(frame2,text="Posicion: ",bg="#ADC4AB",font=self.fuente_consolas_pequeño,fg="#0F1B0D")
        label3.place(x=10,y=150)
        self.entrada3= Entry(frame2,bg="#CACACA",font=self.fuente_consolas_pequeño,fg="#0F1B0D",width=15)
        self.entrada3.place(x=10,y=180)
        label4= Label(frame2,text="Salario: ",bg="#ADC4AB",font=self.fuente_consolas_pequeño,fg="#0F1B0D")
        label4.place(x=10,y=220)
        self.entrada4= Entry(frame2,bg="#CACACA",font=self.fuente_consolas_pequeño,fg="#0F1B0D",width=15)
        self.entrada4.place(x=10,y=250)
        label5= Label(frame2,text="Fecha Contratacion: ",bg="#ADC4AB",font=self.fuente_consolas_pequeño,fg="#0F1B0D")
        label5.place(x=10,y=290)
        self.entrada5= Entry(frame2,bg="#CACACA",font=self.fuente_consolas_pequeño,fg="#0F1B0D",width=15)
        self.entrada5.place(x=10,y=320)

        self.botonGuardar = Button(frame2,text="Guardar",font=self.fuentePequeña,width=10,height=2,bg="#0F1B0D",fg="#CACACA")
        self.botonGuardar.place(x=10,y=360)
        self.botonCancelar = Button(frame2,text="Borrar",font=self.fuentePequeña,width=10,height=2,bg="#0F1B0D",fg="#CACACA")
        self.botonCancelar.place(x=110,y=360)

        self.grid = ttk.Treeview(self.ventana2,columns=("Hotel","Nombre", "Posicion", "Salario", "Fecha de Contratacion"),selectmode="browse")
        self.grid.heading("#1", text="Hotel")
        self.grid.heading("#2", text="Nombre")
        self.grid.heading("#3", text="Posición")
        self.grid.heading("#4", text="Salario")
        self.grid.heading("#5", text="Fecha de Contratación")
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
        
        
        
        
        
        

    