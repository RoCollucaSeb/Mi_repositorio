def calculo_iva(monto, porcentaje=21):
    return monto*(1+(porcentaje/100))

valor=float(input("Ingrese el precio sin iva:"))
iva=float(input("Ingrese el porcentaje de iva:"))

print(calculo_iva(valor,iva))