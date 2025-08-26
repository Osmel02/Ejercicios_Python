lista = [1,2,3,4,5,6,7,8]

#Al menos 1 numero par
es_par = any(lambda x: x%2==0 for x in lista)
if es_par: print("Existe al menos 1 # par")
else: print("No existe ningun numero par")