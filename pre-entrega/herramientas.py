#Importo librería OS para usar el clear screen
import os

#Importo libreria keyboard para validar ENTER / ESC
import keyboard

#Importo sqlite3 para manejo de la bbdd
import sqlite3



 #Limpio pantalla supongo que si no es windows ("nt") es mac/linux ("posix")
def limpiar_pantalla():
   
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    return

def carga_inicial_productos():
    conexion = sqlite3.connect("./pre-entrega/files/productos.db")
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS t_productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        categoria TEXT,
        precio INTEGER NOT NULL CHECK (precio > 0)
        )
    """)

    cursor.execute("SELECT nombre, categoria, precio FROM t_productos")

    productos = cursor.fetchall()
    return(productos)

def graba_productos(productos):

    with open("./pre-entrega/files/productos.txt","w",encoding='utf-8') as archivo:
        for producto in productos:

            linea = ",".join(str(dato) for dato in producto)
            archivo.write(linea + "\n")  
    return

