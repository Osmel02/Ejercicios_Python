def filtrado(criterio,lista):
    return [elemento for elemento in lista if criterio(elemento)]

def es_par(x):
    return x%2 == 0

def es_impar(x):
    return x%2 != 0

lista = [1,2,3,4,5,6,7,8,9,0]

numeros_par = filtrado(es_par,lista)
numeros_impar = filtrado(es_impar,lista)

print(f"Estos son los numeros pares: {numeros_par} y estos los impares: {numeros_impar}")