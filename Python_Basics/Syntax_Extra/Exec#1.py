import time
print("========================= EJERCICIO ADICIONAL ================================")
print("------------------- Calcula descuento de un producto -------------------------")
print()                              #  Imprime una línea en blanco

price = int(input("Digite el precio del producto que deseas aplicar el descuento "))
discount = float(0)                   # Variable que almacena el descuento a aplicar
new_price = float(0)                  # Variable que almacena el nuevo precio

while price <= 0:                     # Validad que el precio el producto sea mayor a 0, si es 0, solicita un nuevo precio
    print()
    print("El precio del producto debe ser mayor a 0")
    price = int(input("Por favor vuelva a digitar un precio de producto mayor a 0 "))
    print()

if price < 100:
    discount = (price * 2) / 100    # Calcula el descuento de un 2% si el precio es menor a 100
    new_price = price - discount    # Calcula el nuevo precio con el desucento
    print()
    print(f"Recibio un 2% de descuento, y el precio final es de: {new_price}")
else:
    discount = (price * 10) / 100  # Calcula el descuento de un 10% si el precio es mayor a 100
    new_price = price - discount    # Calcula el nuevo precio con el desucento
    print()
    print(f"Recibio un 2% de descuento, y el precio final es de: {new_price}")

time.sleep(5)