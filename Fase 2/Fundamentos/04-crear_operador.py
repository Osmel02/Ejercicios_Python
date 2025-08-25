def crear_operador(multiplicador):
    def operar(numero):
        return multiplicador * numero
    return operar

duplicar = crear_operador(2)
triplicar = crear_operador(3)

print(f"El numero 5 se duplicara y triplicara: {duplicar(5)}, {triplicar(5)}")