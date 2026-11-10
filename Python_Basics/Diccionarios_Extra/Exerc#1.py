import time

print("====================== EJERCICIO EXTRA DE DICCIONARIO ================================")
print("---------------------------------Ejercicio #1-----------------------------------------")
print()

sales = []

sales_count = int(input("¿Cuántas ventas desea ingresar? "))

# Pedir los datos de cada venta
for sale_number in range(sales_count):
    print(f"\n--- Venta {sale_number + 1} ---")

    date = input("Fecha de la venta (AAAA-MM-DD): ")
    customer_email = input("Correo del cliente: ")

    items = []
    items_count = int(input("¿Cuántos artículos tiene esta venta? "))

    # Pedir los datos de cada artículo
    for item_number in range(items_count):
        print(f"\nArtículo {item_number + 1}")

        name = input("Nombre: ")
        upc = input("UPC: ")
        unit_price = float(input("Precio unitario: "))

        item = {
            "name": name,
            "upc": upc,
            "unit_price": unit_price
        }

        items.append(item)

    sale = {
        "date": date,
        "customer_email": customer_email,
        "items": items
    }

    sales.append(sale)

# Calcular el total vendido por cada UPC
totals_by_upc = {}

for sale in sales:
    for item in sale["items"]:
        upc = item["upc"]
        unit_price = item["unit_price"]

        if upc not in totals_by_upc:
            totals_by_upc[upc] = 0

        totals_by_upc[upc] += unit_price

# Mostrar cada UPC en una fila diferente
print("\n--- Total de ventas por UPC ---")
print(f"{'UPC':<20} {'Total vendido':>15}")

for upc, total in totals_by_upc.items():
    print(f"{upc:<20} {total:>15.2f}")


time.sleep(5)