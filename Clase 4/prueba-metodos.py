nombre = "   jUan perez  "

print(nombre.strip())
print(nombre.strip().upper())
print(nombre.lower())
print(nombre.title())
print(nombre.strip().capitalize())
print(nombre.strip().replace("jUan","Emilio").title())
print(nombre)

mail = "juancito@gmail.com"
if not mail.find("@")==-1:
    sub= mail[mail.find("@")+1:len(mail)]
    print(sub)

if mail.find("@") == -1:
    print("mail incorrecto")
elif sub.find(".")==-1:
    print("mail incorrecto, falta punto")
else:
    print("mail ok")