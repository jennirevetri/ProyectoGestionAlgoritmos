import tkinter as tk
from tkinter import ttk
import csv

facturas = []

class Factura:
    def __init__(self, id_factura, costo_total, servicios, metodo_pago, estado_pago):
        self.id_factura = id_factura
        self.costo_total = costo_total
        self.servicios = servicios
        self.metodo_pago = metodo_pago
        self.estado_pago = estado_pago

# Función para cargar los datos desde el archivo CSV
def cargar_facturas():
    global facturas  # Agrega esta línea para usar la variable global

    # Borra todos los elementos de la lista facturas
    facturas = []


    with open('facturas.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            factura = Factura(
                int(row['ID_Factura']),
                float(row['Costo_Total']),
                row['Servicios'],
                row['Metodo_Pago'],
                row['Estado_Pago']
            )
            facturas.append(factura)

    return facturas

# Función para insertar una nueva factura
def insertar_factura(id_factura, costo_total, servicios, metodo_pago, estado_pago):
    nueva_factura = Factura(id_factura, costo_total, servicios, metodo_pago, estado_pago)
    facturas.append(nueva_factura)
    guardar_facturas()
    

# Función para eliminar una factura por ID
def eliminar_factura(id_factura):
    global facturas
    facturas = [factura for factura in facturas if factura.id_factura != id_factura]
    guardar_facturas()

    


# Función para modificar una factura por ID
def modificar_factura(id_factura, costo_total, servicios, metodo_pago, estado_pago):
    for factura in facturas:
        if factura.id_factura == id_factura:
            factura.costo_total = costo_total
            factura.servicios = servicios
            factura.metodo_pago = metodo_pago
            factura.estado_pago = estado_pago
    guardar_facturas()
            

# Función para guardar las facturas en el archivo CSV
def guardar_facturas():
    with open('facturas.csv', 'w', newline='') as csvfile:
        fieldnames = ['ID_Factura', 'Costo_Total', 'Servicios', 'Metodo_Pago', 'Estado_Pago']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for factura in facturas:
            writer.writerow({
                'ID_Factura': factura.id_factura,
                'Costo_Total': factura.costo_total,
                'Servicios': factura.servicios,
                'Metodo_Pago': factura.metodo_pago,
                'Estado_Pago': factura.estado_pago
            })


# Cargar las facturas y actualizar la tabla





