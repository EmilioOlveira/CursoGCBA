nombre = input("Ingresa tu nombre: ") 
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
e_mail = input("Ingresa tu e-mail: ")

if len(nombre) > 0:
    print("Tu nombre es: " + nombre)
else:
    print("Nombre: ERROR")

if len(apellido) > 0:
    print("Tu apellido es: " + apellido)
else:
    print("Apellido: ERROR")

if edad.isdigit():
    if int(edad)>17:
        print("Tu edad es:" + edad)
    else:
         print("Edad: ERROR")   
else:
    print("Edad: ERROR")

if len(e_mail)>0 and ("@" in e_mail):
    print("Tu e-mail es: " + e_mail)
else: 
    print("e-mail: ERROR")