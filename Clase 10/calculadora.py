import os
from funciones import *


def menu():
    """
    Muestra el menú interactivo de la calculadora y gestiona las acciones del usuario.

    Limpia la consola según el sistema operativo, procesa la opción elegida,
    solicita los operandos de manera segura y ejecuta la operación matemática
    correspondiente usando el módulo externo.

    Retorna:
        bool: False si el usuario decide salir del programa, None en cualquier otro caso.
    """
    # Limpia la pantalla: 'cls' para Windows (nt) o 'clear' para Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

    print("--- CALCULADORA INTERACTIVA ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    # Captura la opción del usuario eliminando espacios accidentales al inicio o final
    opcion = input("Seleccione una opción: ").strip()

    # Estructura de control para validar la opción antes de pedir los números
    match opcion:
        case "1" | "2" | "3" | "4":
            # Se solicitan los operandos únicamente si se eligió una operación válida
            a = ingresa_numero("primer")
            b = ingresa_numero("segundo")

            match opcion:
                case "1":
                    resultado = suma(a, b)
                    print(f"\nEl resultado de la suma es: {resultado}")
                case "2":
                    resultado = resta(a, b)
                    print(f"\nEl resultado de la resta es: {resultado}")
                case "3":
                    resultado = multiplicacion(a, b)
                    print(f"\nEl resultado de la multiplicación es: {resultado}")
                case "4":
                    resultado = division(a, b)
                    print(f"\nEl resultado de la división es: {resultado}")
            
            input("\nPresione ENTER para continuar...")

        case "5":
            print("\nSaliendo del programa... ¡Hasta luego!")
            return False  # Retorna False para romper el bucle While externo

        case _:
            # Captura cualquier opción que no sea del 1 al 5
            print("\n❌ Opción inválida. Intente nuevamente.")
            input("Presione ENTER para continuar...")


# Bucle principal de ejecución del programa
# Se mantiene activo de forma indefinida mientras la función menu() no devuelva False
while menu() != False:
    continue
