import time

print("====================== EJERCICIO DICCIONARIO ================================")
print("----------------------------Ejercicio 1--------------------------------------")
print()

# Pedir los datos del hotel
hotel_name = input("Ingrese el nombre del hotel: ")
star_count = int(input("Ingrese el número de estrellas: "))
room_count = int(input("¿Cuántas habitaciones desea registrar? "))

# Crear el diccionario del hotel
hotel = {
    "nombre": hotel_name,
    "numero_de_estrellas": star_count,
    "habitaciones": []
}

# Pedir los datos de cada habitación
for i in range(room_count):
    print(f"\nHabitación {i + 1}")

    room_number = int(input("Ingrese el número de habitación: "))
    floor = int(input("Ingrese el piso: "))
    price_per_night = float(input("Ingrese el precio por noche: "))

    room = {
        "numero": room_number,
        "piso": floor,
        "precio_por_noche": price_per_night
    }

    hotel["habitaciones"].append(room)

# Mostrar toda la información
print("\nInformación del hotel:")
print("Nombre:", hotel["nombre"])
print("Número de estrellas:", hotel["numero_de_estrellas"])

for room in hotel["habitaciones"]:
    print()  # Dejar una línea en blanco
    print("Número de habitación:", room["numero"])
    print("Piso:", room["piso"])
    print("Precio por noche:", room["precio_por_noche"])

time.sleep(5)