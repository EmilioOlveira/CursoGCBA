import os

from funciones import *

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')


    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion=input("Seleccione una opción: ")
    a=float(input("Ingrese el primer número: "))
    b=float(input("Ingrese el segundo número: "))


    match opcion.strip():
        case "1":
            resultado = suma(a, b)
            print(f"El resultado de la suma es: {resultado}")
            input("Presione ENTER para continuar...")
        case "2":
            resultado = resta(a, b)
            print(f"El resultado de la resta es: {resultado}")
            input("Presione ENTER para continuar...")
        case "3":
            resultado = multiplicacion(a, b)
            print(f"El resultado de la multiplicación es: {resultado}")
            input("Presione ENTER para continuar...")
        case "4":
            resultado = division(a, b)
            print(f"El resultado de la división es: {resultado}")
            input("Presione E1NTER para continuar...")
        case "5":
            print("Saliendo del programa...")
            return False
        case _:
            print("Opción inválida. Intente nuevamente.")
            input("Presione ENTER para continuar...")

while menu() !=False:
    continue