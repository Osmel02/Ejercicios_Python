# Normalizar nombre
nombre = "Osmel Pillot Leyva"
nombre_normalizado = nombre.strip().title()
print(f"Nombre normalizado: {nombre_normalizado}")

# Generar ID simple
primeras_letras = "".join([palabra[0] for palabra in nombre_normalizado.split()])
print(primeras_letras)

ultimas_letras = "".join([palabra[-1] for palabra in nombre_normalizado.split()])
print(ultimas_letras.upper())

numero = 42
id_usuario = f"{primeras_letras.upper()}{numero:03d}"  # Letras + número con 3 dígitos
print(f"ID generado: {id_usuario}")



vocales = "".join([v for v in nombre if v.lower() in "aeiou"])
print(vocales)