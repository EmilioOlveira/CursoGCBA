
# Programa 5.02
# Lee datos de mi archivo excel "Plazos Fijos.xlsx", hoja "BNA"
# carga las fechas de vencimiento de los plazos fijos y sus importes en un Diccionario "Datos"
# Los sumariza por año y mesen un 2do diccionario "Totales"
# Informa por pantalla los totales por año y mes y crea un excel en el mismo path que el archivo 
# original con los totales por año y mes.

# nota: para poder hacerlo tuve que instalar en python la libreria 

import pandas as pd
import os

nombre_archivo = "C:\\Users\\Emilio\\OneDrive\\Finanzas\\Cierres-Aperturas\\Plazos Fijos UVA.xlsx"

# Convertimos el nombre en una ruta completa real (Ej: C:/Proyectos/tu_archivo.xlsx)
ruta_completa_origen = os.path.abspath(nombre_archivo)
# Ahora sí, extraemos de forma segura la carpeta contenedora
# que usaremos al final para crear el nuevo archivo de totales en el mismo path
carpeta_origen = os.path.dirname(ruta_completa_origen)

#Control de error - exitencia del archivo

if not os.path.isfile(nombre_archivo):
    print(f"\033[3mEl archivo {nombre_archivo} no existe.\033[0m")
    exit()  


nombre_hoja = "bna"

# Cargamos el archivo Excel en un DataFrame de Pandas
df = pd.read_excel(nombre_archivo, sheet_name=nombre_hoja)

# Cargamos los nombres de columnas que vamos a utilizar
col_fecha = "VTO"
col_importe = "Importe"

tabla_estructurada = []

for indice, fila in df.iterrows():
    fecha_valor = fila["VTO"]
    importe_valor = fila[col_importe]
    
    # CONTROL DE VACÍOS O CEROS:
    # pd.isna() detecta si la celda de Excel estaba en blanco
    if pd.isna(importe_valor) or importe_valor == 0:
        break  # Frena la lectura inmediatamente
        
    registro = {
        "fecha": fecha_valor,
        "importe": importe_valor
    }
    tabla_estructurada.append(registro)

# Reemplaza tu 'print(tabla_estructurada)' final por esto:
print("\n--- Resultados de la Tabla Interna ---")
for registro in tabla_estructurada:
    print(registro)

# --- PARTE 2: TOTALIZAR POR AÑO Y MES ---

# Usaremos un diccionario temporal para acumular los totales
acumulador = {}

for registro in tabla_estructurada:
    # 1. Convertimos la fecha a un objeto datetime de Python (por seguridad)
    fecha_obj = pd.to_datetime(registro["fecha"])
    
    # 2. Extraemos el año y el mes
    anio = fecha_obj.year
    mes = fecha_obj.month
    
    # 3. Creamos una clave única para cada combinación de Año y Mes
    clave = (anio, mes)
    
    # 4. Si la combinación ya existe, sumamos el importe. Si no, la iniciamos en 0.
    if clave not in acumulador:
        acumulador[clave] = 0.0
    acumulador[clave] += registro["importe"]

# 5. Pasamos el acumulador a la estructura final que pediste: "Año", "Mes", "Total"
totales_por_mes = []
for (anio, mes), total in acumulador.items():
    totales_por_mes.append({
        "Año": anio,
        "Mes": mes,
        "Total": round(total, 2) # Redondeamos a 2 decimales para que quede limpio
    })

# --- ¡NUEVO: ORDENAR POR AÑO Y MES ASCENDENTE! ---
# Esto ordena la lista primero por el campo "Año" y luego por "Mes"
totales_por_mes.sort(key=lambda x: (x["Año"], x["Mes"]))

# --- 1) PRINT FORMATEADO CON TÍTULOS ---
print("\n" + "="*30)
# Definimos los títulos alineados (Año a la izquierda, Mes al centro, Total a la derecha)
print(f"{'Año':<8}{'Mes':<8}{'Total':>12}")
print("-"*30)

for reg in totales_por_mes:
    # Formateamos las variables para que respeten el mismo ancho de columna
    print(f"{reg['Año']:<8}{reg['Mes']:<8}{reg['Total']:>12.2f}")
print("="*30)

# --- 2) GENERAR EL NUEVO EXCEL EN EL MISMO PATH ---
# Creamos el nombre del nuevo archivo combinando la carpeta original con el nuevo nombre
nombre_nuevo_excel = "Totales por año-mes.xlsx"
ruta_completa_destino = os.path.join(carpeta_origen, nombre_nuevo_excel)

# Convertimos nuestra lista de totales a un DataFrame de Pandas
df_totales = pd.DataFrame(totales_por_mes)

# Lo guardamos en Excel (index=False evita que se guarde una columna extra con los números de fila)
df_totales.to_excel(ruta_completa_destino, index=False, sheet_name="Totales")

print(f"\n💾 ¡Archivo guardado con éxito!")
print(f"📁 Ruta: {ruta_completa_destino}")