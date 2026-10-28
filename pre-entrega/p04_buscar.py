#Programa p04_buscar
#Búsqueda de productos por nombre
#no lo aclaraba la consigna pero permito la búsqueda por mayuscula y minúscula indistinta
#Ej: si el usuario ingresa Pera, pera o PERA le mostrara los datos del producto pera
#    en cualquier combinación en que haya sido ingresado.
#Mostrará el PRIMER ARTICULO coincidente, sin importar si hay otras coincidencias

#Importo librerias, desgraciadamente python no les dá visibilidad hacia abajo
# 
# #Importo librería OS para usar el clear screen
import os

#Importo mi archivo de utilidades
from herramientas import *

Imprimi=False

def Buscar(productos):

    #Limpio pantalla
    limpiar_pantalla()

    #Solicito nomnbre de producto a buscar
    print("-"*50)

    Busqueda = input("Ingrese el nombre a buscar ... ")
    imprimi = False
    #Busco en tabla
    for i in productos:

        if i[0].lower() == Busqueda.lower():

            #Imprimo artículo encontrado con formato tarjeta
            print(f"\n")
            print(f"Artículo:  {i[0]}")
            print(f"Categoría: {i[1]}")
            print(f"Precio:    {i[2]}")
    
            imprimi=True
            break

    if imprimi==False:
        #Si no existe, informo de dicha situación
        print(f"\n")
        print("Producto no encontrado")

    # Cierro la pantalla estéticamente
    print("-"*50)

    # input("Presione cualquier tecla para continuar ...")
    return