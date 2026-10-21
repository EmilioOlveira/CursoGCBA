import os

productos = []

def agregar_producto():
    """ Realiza el alta de productos """
    while True:
        Nombre = input("Ingrese nombre de producto:\t")
        Precio = input("Ingrese precio de producto:\t")

        if nombre == "":
            print("Nombre de producto no puede estar vacío")
            continue
        elif precio == "":
            print("Precio de producto no puede estar vacío")
            continue
        else:
            try:
                precio_num = float(precio)
            except ValueError:
                print("Precio de producto debe ser un número")
                continue

        productos.append({"nombre": nombre, "precio": precio_num})

        print(f"Producto agregado: {nombre} - {precio_num}")

        input("Desea agregar otro producto? (s/n): ")

        if input().lower() != "s":
            break
    
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
