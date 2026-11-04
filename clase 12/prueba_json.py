import json

with open (r"C:\users\Emilio\Documents\CursoGCBA\productos.json","r") as archivo:
    mi_tabla=json.load(archivo)

print(mi_tabla)

mi_tabla.append(["Coca Cola","gaseosa",100])
mi_tabla.append(["Fiat Palio","auto",1500000])

print(mi_tabla)


with open(r"C:\users\Emilio\Documents\CursoGCBA\productos.json","w") as archivo:
    json.dump(mi_tabla,archivo)

print(mi_tabla)
