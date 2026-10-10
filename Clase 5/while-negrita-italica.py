contador = 1 

while contador<=10:
   print (f"\033[3mEl valor del contador es:\033[0m \033[1m{contador}\033[0m")

   contador += 1

print

nombre = ""

while nombre=="":
   nombre=input(f"\033[3mIngresá su nombre:\033[0m").strip()
   
   if nombre!="":
      print(f"\033[3m Ingresaste nombre válido:\033[0m \033[1m{nombre}\033[0m")

