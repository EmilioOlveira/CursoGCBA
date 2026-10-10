#Programa p06_Eliminar_indice
#Repite lógica de P05_eliminar, pero en lugar de buscar un nombre, busca un índice
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

def Eliminar_Indice(productos):

    #Limpio pantalla
    limpiar_pantalla()

    #Inicializo Elimine para que no me de error si no elimino nada
    Elimine=False

    #Solicito nomnbre de producto a eliminar
    print("-"*50)

    Busqueda = input("Ingrese el índice (numérico) a buscar ... ")

    try:
        Busqueda=int(Busqueda)

        if Busqueda>(len(productos)-1) or Busqueda<0:
            #No existe dicha posición, informo de dicha situación y me vuevo al menu ppal
            print(f"\n")
            print("Producto no encontrado")
            return(productos)

        #Imprimo artículo con formato tarjeta
        print(f"\n")
        print(f"Artículo:  {productos[Busqueda][0]}")
        print(f"Categoría: {productos[Busqueda][1]}")
        print(f"Precio:    {productos[Busqueda][2]}")

        Respuesta=input("Escriba BAJA para eliminar, cualquier otra tecla para volver ...")

        #Verifico que el índice sea <= a la longitud de productos
        #Si me confirma con baja (en cualquier combinación mayusc/minusc)
        #Elimino usando el método pop() que me devuelve la instancia de tabla borrada
        #e informo que ha sido eliminado
        if Respuesta.lower()=="baja":
            borrado=productos.pop(Busqueda)
            Elimine=True
            print(f"-"*50)
            print(f"El artículo {Busqueda} - {borrado[0]} ha sido ELIMINADO")
    
        # Cierro la pantalla estéticamente
        print("-"*50)

        # input("Presione cualquier tecla para continuar ...")

        #Devuelvo la nueva tabla

    except ValueError:
        print("Debe ingresar un valor numérico entero. Reintente ... ")

    return(productos)