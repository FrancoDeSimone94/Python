
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
    def __init__ (self):
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
                password='admin',
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
        try:
            self.cursor.execute("SELECT * FROM productos")
            productos = self.cursor.fetchall()
            if productos:
                print("Productos en el inventario:")
                for producto in productos:
                    print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}, Cantidad: {producto[3]}, Categoria: {producto[4]}")
            else:
                print("No hay productos en el inventario")
        except Error as e:
            print(f"Error al mostrar los productos: {e}")
        finally:
            self.menu_principal()
    
    def buscar_producto(self):
        try:
            nombre = input("Ingrese el nombre del producto a buscar: ")
            self.cursor.execute("SELECT * FROM productos WHERE nombre = %s", (nombre,))
            producto = self.cursor.fetchone()
            if producto:
                print(f'ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}, Cantidad: {producto[3]}, Categoria: {producto[4]}')
            else: 
                print("Producto no encontrado")
        except Error as e:

            print(f"Error al buscar el producto: {e}")
        finally:
            self.menu_principal()

    def eliminar_producto(self):

        try:
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            self.cursor.execute("DELETE FROM productos WHERE nombre = %s", (nombre,))
            self.conexion.commit()
            if self.cursor.rowcount > 0:
                print("Producto eliminado exitosamente")
            else:
                print("Producto no encontrado")
        except Error as e:
            print(f"Error al eliminar el producto: {e}")
        finally:
            self.menu_principal()
        
    def actualizar_producto(self):
        try:
            nombre = input("Ingrese el nombre del producto a actualizar: ")
            nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
            nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
            nueva_categoria = input("Ingrese la nueva categoria del producto: ")

            self.cursor.execute("UPDATE productos SET precio = %s, cantidad = %s, categoria = %s WHERE nombre = %s", (nuevo_precio, nueva_cantidad, nueva_categoria, nombre))
            self.conexion.commit()
            if self.cursor.rowcount > 0:
                print("Producto actualizado exitosamente")
            else:
                print("Producto no encontrado")
        except ValueError:
                print("Error: El precio y la cantidad deben ser numeros")
        except Error as e:
            print(f"Error al actualizar el producto: {e}")
        finally:
            self.menu_principal()

    def menu_principal(self):
        
        print("Menu Principal")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Actualizar producto")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")
        if opcion == '1':
            self.agregar_producto()
        elif opcion == '2':
            self.mostrar_productos()
        elif opcion == '3':
            self.buscar_producto()
        elif opcion == '4':
            self.eliminar_producto()
        elif opcion == '5':
            self.actualizar_producto()
        elif opcion == '6':
            self.conexion.close()
            exit(0)
        else:
            print("Opcion invalida, intente de nuevo")
            self.menu_principal()

if __name__ == "__main__":
    inventario = GestionInventario()
    inventario.conectar_base_datos()
    inventario.crear_tabla_productos()
    inventario.menu_principal()
    inventario.agregar_producto()
    inventario.mostrar_productos()
    inventario.buscar_producto()
    inventario.eliminar_producto()
    inventario.actualizar_producto()
    inventario.conexion.close()


# Este es un sistema de gestion de inventario basico, se pueden agregar mas funcionalidades como exportar a excel, importar desde excel, etc.
# Se pueden agregar mas validaciones y mejoras en la interfaz de usuario, como usar tkinter o PyQt para crear una interfaz grafica mas amigable.



