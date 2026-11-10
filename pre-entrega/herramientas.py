#Importo librería OS para usar el clear screen
import os

#Importo libreria keyboard para validar ENTER / ESC
import keyboard

#Importo libreria json para manejo de archivos .json
import json

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
        with open("./pre-entrega/files/productos.json","r",encoding='utf-8') as archivo:
            productos=json.load(archivo)
    except (FileNotFoundError):
            productos=[]

    return(productos)

def graba_productos(productos):

    with open("./pre-entrega/files/productos.json","w",encoding='utf-8') as archivo:
        json.dump(productos, archivo)
