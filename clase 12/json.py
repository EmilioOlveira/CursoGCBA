import json

with (r"C:\users\Emilio\Documents\CursoGCBA\productos.json","r") as archivo:
    mi_tabla=json.load(archivo)

print(mi_tabla)
