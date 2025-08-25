
#Escribir en un archivo
with open("archivo.csv","w", encoding="utf-8") as archivo:
    archivo.write("Laptop,1500\n")
    archivo.write("Mouse,300\n")
    archivo.write("Teclado,550\n")

# Leer un archivo    
with open("archivo.csv","r",encoding="utf-8") as archivo:
    lineas = archivo.read()
    print(lineas.strip().split())
    
# Usar los datos en un diccionario
with open("archivo.csv","r",encoding="utf-8") as archivo:
    productos = []
    valor = []
    carrito = {}
    total = 0
    
    for linea in archivo:
        nombre,precio_str = linea.strip().split(",")
        precio = float(precio_str)
        total += precio
        
        productos.append(nombre)
        valor.append(precio)        
    carrito = dict(zip(productos,valor))
    print(carrito)
    print(total)
    
    print(f"Usted a comprado: {carrito.keys()} por un total de ${total} ")
    
      
    
'''
"w" → escritura (sobrescribe el archivo)
"a" → append (agregar sin sobrescribir)
"r" → lectura
'''