dato = input("Introduzca su nombre ")
dato_normalizado = dato.strip().title().split()
print(dato_normalizado)

alias = "".join(inicial[:1] for inicial in dato_normalizado)
print(alias)

