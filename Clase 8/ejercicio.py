# Comentario solo para modificarlo

productos = {"manzanas": 5, "bananas": 10, "naranjas": 8}

def agregar_producto():
    nombre = input("Ingrese el nombre del producto")

    if nombre in productos: 
        respuesta=("El producto ya existe. Desea modificar el precio?.")
        
        if respuesta.lower()!="s":
            return

    try:
        precio = int(input("Ingrese el precio del producto: "))
    except ValueError:
        print("Por favor, ingrese un número válido para el prec ios.")
        return
       
    productos[nombre] = precio

    print(f"Producto {nombre} agregado con precio {precio}.")   

while True:
    input_usuario = input("¿Desea agregar un producto? (s/n): ")
    if input_usuario.lower() == 's':
        agregar_producto()
    else:
        break
    
    for producto, precio in productos.items():
        print(f"{producto}: {precio}")

