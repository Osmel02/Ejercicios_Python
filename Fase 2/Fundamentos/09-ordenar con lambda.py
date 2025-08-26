personas = [
    {"nombre": "Osmel", "edad": 23},
    {"nombre": "Leslie", "edad": 25},
    {"nombre": "Pepe", "edad": 24}
]

orden_edad = list(sorted(personas,key=lambda x:x['edad']))
orden_nombre = list(sorted(personas,key=lambda x:x['nombre']))

print(f"Orden por edad \n {orden_edad}")
print(f"Orden por nombre \n {orden_nombre}")
