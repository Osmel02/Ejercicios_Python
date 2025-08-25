lista = [-2,1,3,5,30,7,3,2,10,25]

#Comprobacion 1
lista.sort()
print(lista[-1])

# Comprobacion 2
var = 0
for i in lista:
    if  i >= var:
        var=i
print(var)