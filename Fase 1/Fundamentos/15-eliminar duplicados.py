lista = [2,2,3,4,5,5,6,7,8,8,9]

conjunto = set(lista)
tupla = tuple(lista)
diccionario = {}

for index, value in enumerate(lista):
    diccionario[index] = value


print(lista)
print(conjunto)
print(tupla)
print(diccionario)
