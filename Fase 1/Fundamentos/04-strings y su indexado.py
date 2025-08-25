texto = "Otorrinonaringologo"

print(texto[0]) # 1er caracter
print(texto[-1]) # ultimo caracter
print(texto[:3]) # 3 primeros caracteres
print(texto[3:]) # desde indice 3 hasta el final 
print(texto[::3]) # saltando de 3 en 3
print(texto[2:6]) # imprime desde indice 2 hasta 6
print(texto[::-1]) # invierte la cadena

## Los strings son inmutables 
texto = "OTORRI" + texto[6:].upper() 
print(texto)