lista = [1,1,1,1,1,1,2,4,5,7,9,5,6,5,1,9,7,2,2,3]
valor = int(input("Introduzca el valor a buscar: "))
# forma 1

try: 
    print(lista.count(valor))

    #forma 2
    contador = 0
    for i in lista:
        if i == valor: contador+=1

    print(contador)
except ValueError as e:
    print(f"El error es {e}")
except NameError as e:
    print(f"El error es {e}")