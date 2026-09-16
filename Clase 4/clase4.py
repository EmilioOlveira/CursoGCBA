nombre = input("Ingresa tu nombre: ") 
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
e_mail = input("Ingresa tu e-mail: ")

#Validación de nombre y apellido informados
# y los formatea y concatena
nombre_completo = nombre+apellido

if len(nombre)>0 and len(apellido)>0:
    print("Tu nombre completo es: " + nombre_completo.capitalize())
elif len(nombre)==0 and len(apellido)>0:
    print("Debe informar su nombre")
elif len(nombre)>0 and len(apellido)==0:
    print("Debe informar Apellido")
else:
    print("Debe informar Nombre y Apellido")

#if len(apellido) > 0:
#    print("Tu apellido es: " + apellido)
#else:
#    print("Apellido: ERROR")

if edad.isdigit():
    edad=int(edad)
    age=""
    if edad<15:    
        age="niño"
        print("Tu edad es:" + str(edad) + ", eres niño")
    elif edad >= 15 and edad <= 18:
        age="adolescente"
        print("Tu edad es: " + str(edad) + ", eres adolescente")
    else:
        age="adulto"
        print("Tu edad es: " + str(edad) + ", eres adulto")
else:
    print("Edad: ERROR")

if len(e_mail)>0 and ("@" in e_mail):
    print("Tu e-mail es: " + e_mail.strip())
else: 
    print("Debe informar e-mail")

 
match age:
    case "niño":
        print("Tu edad es:" + str(edad) + ", eres niño")
    case "adolescente":
        print("Tu edad es: " + str(edad) + ", eres adolescente")
    case "adulto":
        print("Tu edad es: " + str(edad) + ", eres adulto")
