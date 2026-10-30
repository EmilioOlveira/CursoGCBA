def suma(numero1,numero2):
    try:
        total=numero1+numero2
        return round(total,4)
    except TypeError:
        print("Error: Los parámetros deben ser números.")
        return 0

def resta(numero1,numero2):
    try:
        total=numero1-numero2
        return round(total,4)
    except TypeError:
        print("Error: Los parámetros deben ser números.")
        return 0
def multiplicacion(numero1,numero2):
    try:    
        total=numero1*numero2
        return round(total,4)
    except TypeError:
        print("Error: Los parámetros deben ser números.")
        return 0

def division(numero1,numero2):  
    try:
        total=numero1/numero2
        return round(total,4)
    except TypeError:
        print("Error: Los parámetros deben ser números.")
        return 0
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
        return 0

def ingresa_numero(orden):
    while True:
        try:
            numero = float(input(f"Ingrese el {orden} número: "))
            return numero
        except ValueError:
            print("Error: Debe ingresar un número válido.")