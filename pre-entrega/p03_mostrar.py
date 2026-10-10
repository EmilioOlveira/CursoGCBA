#Programa p03_mostrar
#Listado de productos x pantalla, cada 10 lineas tiene stop
# para permitir la correcta visualización de todos

#Importo librerias, desgraciadamente python no les dá visibilidad hacia abajo
# 
# #Importo librería OS para usar el clear screen
import os

#Importo mi archivo de utilidades
from herramientas import *

def Mostrar(productos):
    #Imprimo títulos
    print("="*70)
    print(f"INDICE  PRODUCTO            CATEGORIA               PRECIO")
    print("="*70)

    contador = 0
    for indice,i in enumerate(productos):
        art_nombre=i[0]
        art_cat=i[1]
        art_precio=i[2]
        contador+=1

        print(f"{indice:<8}{art_nombre:<20}{art_cat:<20}{art_precio:>8}")

        if contador%10==0:
            #Cada 10 lineas, paro y pregunto si desea continuar
            print("="*70)
            respuesta=input("Presione N para volver al Menu Principal, cualquier otra tecla para continuar ")

            # Capturo la tecla
        
            if respuesta == "N" or respuesta=="n":     
                break
            else:
                limpiar_pantalla()

    print("="*70)        

    return
