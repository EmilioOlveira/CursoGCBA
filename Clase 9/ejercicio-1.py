import os

productos = []

def agregar_producto():
    """ Realiza el alta de productos """
    while True:
        nombre = input("Ingrese nombre de producto:\t")
        precio = input("Ingrese precio de producto:\t")

        if nombre == "":
            #Error: El nombre del producto no puede estar vacío

            print("Nombre de producto no puede estar vacío")
            input()
        elif precio == "":
            #Error: El precio del producto no puede estar vacío

            print("Precio de producto no puede estar vacío")
            input()
        else:
            try:
                #Valido precio numérico
                precio_num = float(precio)

                # Acá agrego producto ya que cumple todos los requisitos
                productos.append([nombre, precio_num])

                print(f"Producto agregado: {nombre} - {precio_num}")
                
            except ValueError:
                #Error: El precio del producto debe ser un número

                print("Precio de producto debe ser un número")
                input()

        opcion=input("Desea agregar otro producto? (s/n): ")

        if opcion.lower() != "s":
            break
    
    return

def consultar_productos():
    """ Realiza la consulta de productos """

    print("Listado de productos:")
    print(f"-"*50)
    print(f"    Nombre\t\t\tPrecio")
    for producto in productos:
        print(f"{producto[0]:<20}\t\t\t{producto[1]:>12.2f}")
    input("Presione Enter para continuar...")

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
