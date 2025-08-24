cadena = "murcielago"
lista = ['a','e','i','o','u']
contador = 0

for v in cadena:
    if v in lista:
        contador += 1
        
print(f"La palabra {cadena} tiene {contador} vocales")