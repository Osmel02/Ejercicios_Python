while True:
    numero = int(input("Introduzca hasta donde quiere sumar: "))
    valor = 0
    for n in range(1,numero+1):
        valor += n
    print(f"La suma hasta el numero {numero} es: {valor}")
    break
