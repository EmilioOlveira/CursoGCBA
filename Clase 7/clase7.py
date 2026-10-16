def calcula_promedio(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio

ventas_semanales = [150,200,250,300,100,180,220]

primeros_dias = ventas_semanales[:3]
ultimos_dias = ventas_semanales[-2:]
medios_dias = ventas_semanales[3:5]

print(f"Promedio primeros tres días: {str(calcula_promedio(primeros_dias))}")

print(primeros_dias)

print(f"Promedio medios días: {str(calcula_promedio(medios_dias))}")
print(f"Suma medios dias: "+ str(sum(medios_dias)))
print(medios_dias)

print(f"Promedio últimos dos días: {str(calcula_promedio(ultimos_dias))}")

print(ultimos_dias)

