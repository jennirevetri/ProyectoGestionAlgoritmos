import tkinter as tk
from tkinter import ttk
import csv

class Employee:
    def __init__(self, hotel, nombre, posicion, salario, fecha_contratacion):
        self.hotel = hotel
        self.nombre = nombre
        self.posicion = posicion
        self.salario = salario
        self.fecha_contratacion = fecha_contratacion
        self.left = None
        self.right = None

class EmployeeTree:
    def __init__(self):
        self.root = None

    def insert(self, hotel, nombre, posicion, salario, fecha_contratacion):
        new_employee = Employee(hotel, nombre, posicion, salario, fecha_contratacion)
        if self.root is None:
            self.root = new_employee
        else:
            self._insert_recursively(self.root, new_employee)

    def _insert_recursively(self, current_node, new_employee):
        if new_employee.nombre < current_node.nombre:
            if current_node.left is None:
                current_node.left = new_employee
            else:
                self._insert_recursively(current_node.left, new_employee)
        else:
            if current_node.right is None:
                current_node.right = new_employee
            else:
                self._insert_recursively(current_node.right, new_employee)

    def in_order_traversal(self, node, treeview):
        if node:
            self.in_order_traversal(node.left, treeview)
            treeview.insert("", "end", values=(node.hotel, node.nombre, node.posicion, node.salario, node.fecha_contratacion))
            self.in_order_traversal(node.right, treeview)

    def eliminar(self, nombre_empleado):
        self.root = self._eliminar_recursivamente(self.root, nombre_empleado)

    def _eliminar_recursivamente(self, current_node, nombre_empleado):
        if current_node is None:
            return current_node

        # Recorrer el árbol de forma recursiva para encontrar el nodo a eliminar
        if nombre_empleado < current_node.nombre:
            current_node.left = self._eliminar_recursivamente(current_node.left, nombre_empleado)
        elif nombre_empleado > current_node.nombre:
            current_node.right = self._eliminar_recursivamente(current_node.right, nombre_empleado)
        else:
            # Encontramos el nodo a eliminar
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            # Si el nodo tiene dos hijos, encontrar el sucesor inmediato en el subárbol derecho
            current_node.nombre = self._encontrar_minimo(current_node.right).nombre

            # Eliminar el sucesor inmediato
            current_node.right = self._eliminar_recursivamente(current_node.right, current_node.nombre)

        return current_node

    def _encontrar_minimo(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def modificar(self, nombre_empleado, nuevo_nombre, nueva_posicion, nuevo_salario, nueva_fecha_contratacion):
        self.root = self._modificar_recursivamente(self.root, nombre_empleado, nuevo_nombre, nueva_posicion, nuevo_salario, nueva_fecha_contratacion)

    def _modificar_recursivamente(self, current_node, nombre_empleado, nuevo_nombre, nueva_posicion, nuevo_salario, nueva_fecha_contratacion):
        if current_node is None:
            return current_node

        # Busca el nodo con el empleado que deseas modificar
        if nombre_empleado < current_node.nombre:
            current_node.left = self._modificar_recursivamente(current_node.left, nombre_empleado, nuevo_nombre, nueva_posicion, nuevo_salario, nueva_fecha_contratacion)
        elif nombre_empleado > current_node.nombre:
            current_node.right = self._modificar_recursivamente(current_node.right, nombre_empleado, nuevo_nombre, nueva_posicion, nuevo_salario, nueva_fecha_contratacion)
        else:
            # Encontramos el nodo a modificar
            current_node.nombre = nuevo_nombre
            current_node.posicion = nueva_posicion
            current_node.salario = nuevo_salario
            current_node.fecha_contratacion = nueva_fecha_contratacion

        return current_node

def cargar_empleados(file_path, employee_tree):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            hotel = row['Hotel']
            nombre = row['Nombre']
            posicion = row['Posicion']
            salario = row['Salario']
            fecha_contratacion = row['Fecha de Contratacion']
            employee_tree.insert(hotel, nombre, posicion, salario, fecha_contratacion)




