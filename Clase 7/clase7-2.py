mi_lista = []
respuesta = ""

while respuesta.lower() != "fin":

    respuesta = input("Ingrese un nombre o fin para terminar: ")
    if respuesta.strip() == "":
        print("No se puede ingresar un nombre vacío. Intente nuevamente.")
        continue    

    mi_lista.append(respuesta)

    if respuesta.lower() != "fin":
        break

mi_lista.sort()

for i in mi_lista:
    print(i)