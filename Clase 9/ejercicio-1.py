import os

productos = []

def agregar_producto():
    """ Realiza el alta de productos """
    print("alta de productos")
    return

def consultar_productos():
    """ Realiza la consulta de productos """
    print("consulta de productos")

    return

def eliminar_producto():
    """ Realiza la eliminación de productos """
    print("eliminación de productos")

    return

def mostrar_menu():
    """ Muestra el menú de opciones """

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Bienvenido al sistema de gestión de productos")
        print(f"Agregar producto)")
        print(f"Consultar producto")
        print(f"Eliminar producto")
        print(f"Salir")

        opcion = input("Seleccione una opción: (letra mayuscula)")

        match opcion.lower(): 
            case "s":
                print("Saliendo del sistema...")
                break
            case "a":
                agregar_producto()
            case "c":
                consultar_productos()
            case "e":
                eliminar_producto()

    return            
     
            
mostrar_menu()
