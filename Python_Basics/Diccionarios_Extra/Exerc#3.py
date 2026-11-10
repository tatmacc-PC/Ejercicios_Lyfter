import time

print("====================== EJERCICIO EXTRA DE DICCIONARIO ================================")
print("---------------------------------Ejercicio #3-----------------------------------------")
print()

products = []
sales = {}

# Pedir los productos vendidos
while True:
    name = input("\nNombre del producto (o 'fin' para terminar): ").strip()

    if name.lower() == "fin":
        break

    if not name:
        print("El nombre no puede estar vacío.")
        continue

    category = input("Categoría del producto: ").strip().capitalize()

    if not category:
        print("La categoría no puede estar vacía.")
        continue

    # Validar el precio
    while True:
        try:
            price = float(input("Precio del producto: "))

            if price < 0:
                print("El precio no puede ser negativo.")
                continue

            break
        except ValueError:
            print("Ingrese un número válido, por ejemplo: 200.50")

    products.append({
        "name": name,
        "category": category,
        "price": price
    })

# Acumular la cantidad y el total vendido por categoría
for product in products:
    category = product["category"]
    price = product["price"]

    if category not in sales:
        sales[category] = {
            "quantity": 0,
            "total": 0
        }

    sales[category]["quantity"] += 1
    sales[category]["total"] += price

# Calcular el promedio y mostrar los resultados
print("\nRESULTADOS POR CATEGORÍA")

if not sales:
    print("No se ingresaron productos.")
else:
    for category, data in sales.items():
        data["average"] = data["total"] / data["quantity"]

        print(
            f"{category}: "
            f"Productos: {data['quantity']} | "
            f"Total vendido: {data['total']:.2f} | "
            f"Promedio: {data['average']:.2f}"
        )

time.sleep(5)