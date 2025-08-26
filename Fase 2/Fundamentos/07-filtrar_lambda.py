lista = [1,2,3,4,5,6,7,8,9,10,11,12,13]

numeros_pares= list(filter(lambda x: x%2==0,lista))
numeros_inveritdos = lambda x: 1/x if x !=0 else "Error"

print(f"Estos son los numeros pares {numeros_pares}")
for n in lista:
    print(numeros_inveritdos(n))