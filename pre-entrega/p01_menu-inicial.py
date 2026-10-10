#Programa 01-menu-inicial
#Muestra y maneja el menú de productos

#Importo (en cada programa), el archivo "Herramientas.py"
#que tiene funciones generales que quiero usar
#Uso el import *, porque son funciones generales. 

from herramientas import *

#Importo todas las funciones donde ejecutaré cada opción del menú 
#Están en archivos separados para claridad de código

from p02_altas import Alta
from p03_mostrar import Mostrar
from p04_buscar import Buscar
from p05_eliminar import Eliminar
from p06_eliminar_indice import Eliminar_Indice


#Librerías
#Para poder usarlas, primero tuve que instalarlas en Python
#con comando de estructura python -m pip install keyboard
#fuera de VSC, llamaqndo a un cmd
#No sé si se puede hacer también desde VSC, a probar.

#Importo librería OS para usar el clear screen
import os

#Importo libreria keyboard para validar ENTER / ESC

#####################################################
# MUY IMPORTANTE!!!!! --- NO CORRE BIEN DENTRO DE VSC
# HAY QUE CAMBIAR terminal.exploreKind a "External"
# dentro de Archivo/Preferencias/Configuración
#####################################################
import keyboard

# define la tabla de productos
columnas = 3
productos = []

def despliegamenu():
    print("="*30)
    print("       Menú de Productos")
    print("="*30)

    print(f"\033[1m1\033[0m - Alta de Productos")
    print(f"\033[1m2\033[0m - Mostrar Producto")
    print(f"\033[1m3\033[0m - Buscar Producto")
    print(f"\033[1m4\033[0m - Eliminar por Nombre")
    print(f"\033[1m5\033[0m - Eliminar por Indice")     
    print(f"\033[1mS\033[0m - Salir")
    print("\n")
    return

# Inicializo productos para prueba (linea a asterisquear)
# productos=[["pera","fruta",10],["Manzana","fruta",20],["apio","verdura",30]]

#Bucle eterno (hasta el break x opción salida)
while True:
    #Limpio pantalla para que siempre el menú aparezca igual y en la misma posición
    limpiar_pantalla()

    # Despliego menu
    despliegamenu()

    # Solicito al usuario que ingrese su opción y manejo el error si no es un número
    
    Entrada=input ("\033[1mIngrese su opción:\033[0m")

    try:       
        Opcion = int(Entrada)
    except ValueError:
        #Tomo solo el primer caracter y lo convierto a mayusculas, si escribe SALIDA va a salir, si escribe TOLDO, no
        Opcion = Entrada[0].upper()
    
    # Llama a las distintas opciones del menú según la elección del usuario
    match Opcion:
        case 1:
            productos=Alta(productos)
        case 2:
            Mostrar(productos)
        case 3:
            Buscar(productos)
        case 4:
            productos=Eliminar(productos)
        case 5:
            productos=Eliminar_Indice(productos)
        case "S":
            break
        case _:
            print ("Opción Inválida")

    # Pido un Enter para continuar. En realidad con cualquier tecla va a avanzar, es solo para parar
    # y que el usuario pueda ver la salida de su opción antes de continuar
    #No necesito validar nada, cualquier tecla continúa. Solo "S" Sale.

    print("\n")
    input("Presione ENTER para continuar...") 




    


