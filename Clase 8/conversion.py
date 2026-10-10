def Fecha_a_texto(dia,mes,anio):

    Meses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
    dias= ("Uno","Dos","Tres","Cuatro","Cinco","Seis",
        "Siete","Ocho","Nueve","Diez","Once","Doce","Trece",
        "Catorce","Quince","Dieciseis","Diecisiete","Dieciocho",
        "Diecinueve","Veinte","Veintiuno","Veintidos","Veintitres", 
        "Veinticuatro","Veinticinco","Veintiseis","Veintisiete","Veintiocho","Veintinueve",
        "Treinta","Treinta y uno")

    if dia.isnumer()==False or mes.isnumer()==False or anio.isnumer()==False:
        return "Fecha inválida"
    
    if dia <1 or dia >31 or (mes==2 and dia>29) or (mes in [4,6,9,11] and dia>30):
        return "Fecha inválida"
    elif mes<1 or mes>12
        return "Fecha inválida"
    elif anio<0
        return "Fecha Inválida"

    Fecha = dias[dia-1] + " de " + Meses[mes-1] + " de " + str(anio)

    return Fecha


fecha_ingresada=input("Ingrese Fecha en formato dd/mm/aaaa:")

dia=int(fecha_ingresada[0:2])
mes=int(fecha_ingresada[3:5])
anio=int(fecha_ingresada[6:10])

fecha_str= Fecha_a_texto(dia,mes,anio)

print(f"Mi fecha es:{fecha_str}")