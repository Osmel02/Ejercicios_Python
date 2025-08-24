# Catálogo usando dict
catalogo = {
    101: {"nombre": "Laptop", "precio": 1500},
    102: {"nombre": "Mouse", "precio": 25},
    103: {"nombre": "Teclado", "precio": 50}
}

# Carrito usando list
carrito = []

# Agregar productos
carrito.append(catalogo[101])
carrito.append(catalogo[103])

# Calcular total
total = sum(item["precio"] for item in carrito)
print("Productos en el carrito:")
for item in carrito:
    print("-", item["nombre"], f"${item['precio']}")
print(f"Total: ${total}")