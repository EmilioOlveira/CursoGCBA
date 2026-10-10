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
