import time

print("====================== EJERCICIO EXTRA DE DICCIONARIO ================================")
print("---------------------------------Ejercicio #2-----------------------------------------")
print()

# Crear el diccionario para agrupar empleados por departamento
departments = {}

# Pedir y validar la cantidad de empleados
while True:
    text = input("¿Cuántos empleados desea ingresar? ").strip()

    if text.isdecimal() and int(text) > 0:
        employee_count = int(text)
        break

    print("Ingrese un número entero mayor que cero.")

# Pedir los datos de cada empleado
for index in range(employee_count):
    print(f"\nEmpleado {index + 1}")

    name = input("Nombre: ").strip()
    email = input("Correo: ").strip()
    department = input("Departamento: ").strip().capitalize()

    employee = {
        "name": name,
        "email": email
    }

    # Crear la lista si el departamento todavía no existe
    if department not in departments:
        departments[department] = []

    # Agregar el empleado a su departamento
    departments[department].append(employee)

# Mostrar cada empleado en una fila, agrupado por departamento
print("\nEMPLEADOS POR DEPARTAMENTO")

for department, employees in departments.items():
    print(f"\nDepartamento: {department}")
    print(f"{'Nombre':<25} | Correo")
    print("-" * 55)

    for employee in employees:
        print(f"{employee['name']:<25} | {employee['email']}")

time.sleep(5)