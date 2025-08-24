distancia = float(input("Introduzca la distancia a recorrer: "))

if distancia <= 100:
    print("Debe pagar $500")
elif distancia > 100 and distancia < 500:
    print("Debe pagar $750")
else:
    print("Debe pagar $1000")