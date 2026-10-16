mi_lista = []
respuesta = ""

while True:

    respuesta = input("Ingrese un nombre o fin para terminar: ")
    if respuesta.strip() == "":
        print("No se puede ingresar un nombre vacío. Intente nuevamente.")
        continue    

    if respuesta.lower() == "fin":
        break

    mi_lista.append(respuesta)


mi_lista.sort()

for i in mi_lista:
    print(i)