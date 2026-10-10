#Programa p02_altas
#Alta de productos, incluye validación del precio

#Importo librerias, desgraciadamente python no les dá visibilidad hacia abajo
# 
# #Importo librería OS para usar el clear screen
import os

#Importo mi archivo de utilidades
from herramientas import *

#Defino tupla en donde guardo los textos de los códigos de error
#
#El orden es inverso, para usar la posibildiad de ubicar elementos por su índice negativo
#Ej. Errores precios(-1) me devolverá "Error - El precio debe ser entero"
#
#Nota: Es una tupla, ergo, sus valores son constantes

Errores_precio=("Error - El precio debe ser numérico", 
                "Error - El precio debe ser positivo",
                "Error - Debe informar Precio <> 0", 
                "Error - El precio debe ser entero")


def valida_precio(precio):
    mi_precio=0
    try:
        mi_precio=float(precio)
    except ValueError:
                return -4           #No es númerico
    
    if mi_precio.is_integer():
        if mi_precio>0:
            return int(precio)  #Devuelve precio en formato entero
        elif mi_precio==0:
            return -2           #Devuelve error -2 - Precio es cero   
        elif mi_precio<0:
            return -3           #Devuelve error -1 - Precio es negativo
    else:
        return -1               #Devuelve error -3 - Precio no es entero


def Alta(productos):

    while True:
        #Limpio pantalla del menú/carga anterior
        limpiar_pantalla()
     
        art_nombre= input("\033[1mIngrese nombre:\033[0m")
        art_cat=    input("\033[1mIngrese categoría:\033[0m")
        art_precio= input("\033[1mIngrese precio: \033[0m")

        ok=valida_precio(art_precio)

        print(f"\n")    #linea en blanco
        if ok>0:
            productos.append([art_nombre,art_cat,int(art_precio)])
            print(f"\033[1mProducto {art_nombre} cargado OK.\033[0m")
                   
        else:
            print(f"{Errores_precio[ok]}\n")
            
        #Pregunto si quiere salir ("N") o seguir cargando
        
        respuesta=input("Presione 'N' para volver al Menu Principal, cualquier otra tecla para continuar ")

        if respuesta == "N" or respuesta=="n":     
            break

    return(productos) 