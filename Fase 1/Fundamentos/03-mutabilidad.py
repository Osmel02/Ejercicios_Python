# Mutable
lista = [1, 2, 3]
lista.append(4)
print(lista)  # [1, 2, 3, 4]

# Inmutable
texto = "Hola"
# texto[0] = "h"  <- ERROR, no se puede modificar
texto = "h" + texto[1:]  # se crea una nueva cadena
print(texto)  # hola
