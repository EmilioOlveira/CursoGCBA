import json

with open (r"C:\users\Emilio\Documents\CursoGCBA\productos.json","r") as archivo:
    mi_tabla=json.load(archivo)

print(mi_tabla)

mi_tabla.append({"nombre":"Coca Cola","precio":150,"stock":100})
mi_tabla.append({"nombre":"Fiat Palio","precio":1500000,"stock":10})

with open(r"C:\users\Emilio\Documents\CursoGCBA\productos.json","w") as archivo:
    json.dump(mi_tabla,archivo,indent=4)

print(mi_tabla)
