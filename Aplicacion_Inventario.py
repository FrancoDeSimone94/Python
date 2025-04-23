
# Sistema de gestion con python y base de datos mysql
# (La base no la tengo instalada ni configurada)
# tiene que agregar productos
# mostrar todos los productos
# tiene que buscar productos por nombre
# tiene que eliminar productos
# tiene que actualizar productos

# Usar una base de datos mysql para almacenar la informacion
# imprementar operaciones CRUD (Create, Read, Update, Delete)
# utilizar la bliblioteca mysql-connector-python para conectarse a la base de datos
# implementar un menu de opciones para el usuario
# implementar gestion de errores para manejar excepciones como intentar agregar un nombre que ya existe, intentar buscar actualziar 
# o eliminar un producto que ya existe, manejar errores de conexion a la base de datos, etc.


import mysql.connector
from mysql.connector import Error
import os
import time
import getpass
import random
import string

# Definicion de la clase producto

class Producto:
    def __init__(self):
        self.nombre = None
        self.precio = None
        self.cantidad = None
        self.categoria = None

# Definicion de la clase GestionInventario que tenga los metodos para agregar, mostrar, buscar, eliminar y actualizar productos
class GestionInventario:
    def __init__ self():
        self.conexion = None
        self.cursor = None
        self.conectar_base_datos()
        self.crear_tabla_productos()
        self.productos = []
        self.menu_principal()
        self.agregar_producto()
        self.mostrar_productos()
        self.buscar_producto()
        self.eliminar_producto()
        self.actualizar_producto()
    
    
    def conectar_base_datos(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='inventario'
            )
            if self.conexion.is_connected():
                print("Conectado a la base de datos")
                self.cursor = self.conexion.cursor()
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            exit(1)

    def crear_tabla_productos(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS productos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(255) NOT NULL UNIQUE,
                    precio DECIMAL(10, 2) NOT NULL,
                    cantidad INT NOT NULL,
                    categoria VARCHAR(255) NOT NULL
                )
            """)
            self.conexion.commit()
        except Error as e:
            print(f"Error al crear la tabla de productos: {e}")
            exit(1)
    
    def agregar_producto(self):
        try:
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            categoria = input("Ingrese la categoria del producto: ")

            self.cursor.execute("INSERT INTO productos (nombre, precio, cantidad, categoria) VALUES (%s, %s, %s, %s)", (nombre, precio, cantidad, categoria))
            self.conexion.commit()
            print("Producto agregado exitosamente")
        except mysql.connector.IntegrityError:
            print("Error: El producto ya existe")
        except ValueError:
            print("Error: El precio y la cantidad deben ser numeros")
        except Error as e:
            print(f"Error al agregar el producto: {e}")
        finally:
            self.menu_principal()

    def mostrar_productos(self):

