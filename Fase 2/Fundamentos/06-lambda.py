doble = lambda x: x*2
triple = lambda x: x*3
invertir = lambda x: 1/x if x != 0 else "Error"

num = 8
print("Invertido: ",invertir(num),"Doble: ",doble(num), "Triple: ", triple(num), sep="\n")