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

def graba_productos(mi_nombre, mi_categoria, mi_precio):

    respuesta=0
        
    #Establezco conexión con la BBDD
    conexion = sqlite3.connect("./pre-entrega/files/productos.db")
    cursor = conexion.cursor()
    
    #Ejecuto mi instrucción para AGREGAR registro

    conexion.execute(
        """ INSERT INTO t_productos (nombre, categoria, precio) 
                VALUES (?,?,?)"""  ,
                (mi_nombre, mi_categoria, mi_precio)
                
    )
    respuesta=cursor.rowcount   # Devuelve 1 si se insertó correctamente, 0 si hubo un error

    print(f"graba_productos: respuesta={respuesta}")
    input("Presione cualquier tecla para continuar ...")

    #Hago commit para que se guarden los cambios y cierro la conexión
    conexion.commit()
    conexion.close()

    return respuesta

def borra_productos(mi_nombre):

    #Este lower es redundante, pero por las dudas es mejor incluirlo

    buscar = mi_nombre.title()

    #Establezco conexión con la BBDD
    conexion = sqlite3.connect("./pre-entrega/files/productos.db")
    cursor = conexion.cursor()

    # Ejcuto el delete limitando al primer registro coincidente, 
    # No debería haber mas de uno, pero por las dudas lo limito a 1

    cursor.execute(
    """ DELETE FROM t_productos 
        WHERE id = (
            SELECT id FROM t_productos WHERE nombre = ? LIMIT 1
        ) """,
    (buscar,),
    )

    if cursor.rowcount > 0:
        print("Producto eliminado con éxito.")
    else:
        print(buscar)
        print("No se encontró ningún producto con ese nombre.")

    input("Presione cualquier tecla para continuar ...")

    #Hago commit para que se guarden los cambios y cierro la conexión
    conexion.commit()
    conexion.close()



