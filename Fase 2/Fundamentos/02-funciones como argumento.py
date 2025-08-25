def asignar_operacion(operacion,numero):
    return operacion(numero)

def duplicar(x):
    return x*2

def triplicar(x):
    return x*3

resultado_1 = asignar_operacion(duplicar,5)
resultado_2 = asignar_operacion(triplicar,10)
print(resultado_1)
print(resultado_2)

