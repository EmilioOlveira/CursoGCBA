#Programa p05_Eliminar
#Repite lógica de P04_buscar
#
#Una vez encontrado y mostrado el producto, pide confirmación de eliminación
#y elimina el artículo solicitado de la tabla

#Importo librerias, desgraciadamente python no les dá visibilidad hacia abajo
# 
# #Importo librería OS para usar el clear screen
import os

#Importo mi archivo de utilidades
from herramientas import *

Imprimi=False

def Eliminar(productos):

    #Limpio pantalla
    limpiar_pantalla()

    #Inicializo Elimine para que no me de error si no elimino nada
    Elimine=False

    #Solicito nomnbre de producto a eliminar
    print("-"*50)

    Busqueda = input("Ingrese el nombre a buscar ... ")

    #Busco en tabla, con enumerate para que me devuelva también en índice en cada iteración
    for indice, i in enumerate(productos):

        if i[0].lower() == Busqueda.lower():

            #Imprimo artículo encontrado con formato tarjeta
            print(f"\n")
            print(f"Artículo:  {i[0]}")
            print(f"Categoría: {i[1]}")
            print(f"Precio:    {i[2]}")

            Respuesta=input("Escriba BAJA para eliminar, cualquier otra tecla para volver ...")

            #Si me confirma con baja (en cualquier combinación mayusc/minusc)
            #Elimino usando el método pop() que me devuelve la instancia de tabla borrada
            #e informo que ha sido eliminado

            if Respuesta.lower()=="baja":
                borrado=productos.pop(indice)
                Elimine=True
                print(f"-"*50)
                print(f"El artículo {indice} - {borrado[0]} ha sido ELIMINADO")
    
    if Elimine==False:
        #Si no existe, informo de dicha situación
        print(f"\n")
        print("Producto no encontrado")

    # Cierro la pantalla estéticamente
    print("-"*50)

    # input("Presione cualquier tecla para continuar ...")

    #Devuelvo la nueva tabla
    return(productos)