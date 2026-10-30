def suma(numero1, numero2):
    """
    Calcula la suma de dos números y redondea el resultado a 4 decimales.

    Argumentos:
        numero1 (int, float): El primer sumando.
        numero2 (int, float): El segundo sumando.

    Retorna:
        float: El resultado de la suma redondeado o 0 si ocurre un error de tipo.
    """
    try:
        total = numero1 + numero2
        return round(total, 4)  # Evita errores de precisión flotante truncando a 4 decimales
    except TypeError:
        # Se ejecuta si alguno de los parámetros no es un número (ej. una cadena de texto)
        print("Error: Los parámetros deben ser números.")
        return 0


def resta(numero1, numero2):
    """
    Calcula la resta entre dos números y redondea el resultado a 4 decimales.

    Argumentos:
        numero1 (int, float): El minuendo.
        numero2 (int, float): El sustraendo.

    Retorna:
        float: El resultado de la resta redondeado o 0 si ocurre un error de tipo.
    """
    try:
        total = numero1 - numero2
        return round(total, 4)
    except TypeError:
        print("Error: Los parámetros deben ser números.")
        return 0


def multiplicacion(numero1, numero2):
    """
    Calcula el producto de dos números y redondea el resultado a 4 decimales.

    Argumentos:
        numero1 (int, float): El primer factor.
        numero2 (int, float): El segundo factor.

    Retorna:
        float: El resultado de la multiplicación redondeado o 0 si ocurre un error de tipo.
    """
    try:    
        total = numero1 * numero2
        return round(total, 4)
    except TypeError:
        print("Error: Los parámetros deben ser números.")
        return 0


def division(numero1, numero2):  
    """
    Calcula el cociente de la división de dos números y redondea a 4 decimales.

    Argumentos:
        numero1 (int, float): El dividendo.
        numero2 (int, float): El divisor.

    Retorna:
        float: El resultado de la división redondeado o 0 si se genera una excepción.
    """
    try:
        total = numero1 / numero2
        return round(total, 4)
    except TypeError:
        print("Error: Los parámetros deben ser números.")
        return 0
    except ZeroDivisionError:
        # Controla específicamente el caso en que el segundo número sea exactamente 0
        print("Error: No se puede dividir por cero.")
        return 0


def ingresa_numero(orden):
    """
    Solicita de forma interactiva un número por consola forzando su ingreso correcto.

    Utiliza un bucle infinito que no se interrumpe hasta que el usuario
    escriba un valor convertible a tipo flotante.

    Argumentos:
        orden (str): Texto indicativo de la posición del número (ej. 'primer', 'segundo').

    Retorna:
        float: El número válido ingresado por el usuario.
    """
    while True:
        try:
            # Intenta capturar la entrada de texto y transformarla inmediatamente a decimal
            numero = float(input(f"Ingrese el {orden} número: "))
            return numero  # Rompe el bucle implícitamente al retornar el valor
        except ValueError:
            # Se activa si el usuario ingresa letras, símbolos o deja el espacio en blanco
            print("Error: Debe ingresar un número válido.")
