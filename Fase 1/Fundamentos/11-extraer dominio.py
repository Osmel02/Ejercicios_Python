correo = input("Introudzca su correo electronico: ")
if "@" in correo:
    correo = correo.strip().lower().split("@")
    print(f"El dominio del correo es {correo[1]}")
else:
    print("El correo no es valido")
    