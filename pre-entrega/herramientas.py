#Importo librería OS para usar el clear screen
import os

#Importo libreria keyboard para validar ENTER / ESC
import keyboard

 #Limpio pantalla supongo que si no es windows ("nt") es mac/linux ("posix")
def limpiar_pantalla():
   
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    return

def carga_inicial_productos():

    #El Try es por si no existe el archivo.

    try:
        with open("./pre-entrega/files/productos.txt","r",encoding='utf-8') as archivo:
            productos=[linea.strip().split(',') for linea in archivo.readlines()]
    except (FileNotFoundError):
            productos=[]
    print(productos)
    input("Presione ENTER para continuar...")

    return(productos)

def graba_productos(productos):

    with open("./pre-entrega/files/productos.txt","w",encoding='utf-8') as archivo:
        for producto in productos:

            linea = ",".join(str(dato) for dato in producto)
            archivo.write(linea + "\n")  
    return

