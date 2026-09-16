nombreCompleto = input("Ingresa tu nombre: ") + input("y tu apellido: ")
edad = int(input("Ingresa tu edad: "))
anioActual = 2026

print(nombreCompleto, ", tu año de nacimiento es: ", anioActual-edad)
print(f"{nombreCompleto}, tu año de nacimiento es: {anioActual-edad}")
print(f"{nombreCompleto}\t\t, tu año de nacimiento es: {anioActual-edad}")
print(f"{nombreCompleto}\t\t, tu año de nacimiento es:\n{anioActual-edad}")

print(nombreCompleto, ", tu año de nacimiento es:", end=str(anioActual-edad)) # Uso de end y str()

print(f"\nTipo de variables: \n Nombre Completo \t\t {type(nombreCompleto)} \n Año Actual\t\t\t {type(anioActual)}")
