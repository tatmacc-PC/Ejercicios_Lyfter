print("============================== EJERCICIO DE FUNCIONES ================================")
print("-----------------------------------Ejercicio #3---------------------------------------")
print()

import time

def get_numbers(): #Función para obtener los números del usuario
    while True:
        text = input("Ingrese una lista de números separados por comas: ")
        parts = text.split(",")
        numbers = []

        try:
            for part in parts:
                number = float(part.strip())
                numbers.append(number)

            return numbers

        except ValueError:
            print("Error: Asegúrese de ingresar solo números separados por comas. Intente nuevamente.")
            print("Para decimales, utilice el punto (.) como separador decimal. Ejemplo: 1.5, 2.3, 3.0")
            print()

def sum_numbers(numbers):  #Función para sumar los números
    total = 0

    for number in numbers:
        total += number

    return total

#Pedir al usuario que ingrese los números
numbers = get_numbers()

#Sumar y guardar el valor retornado en una variable
result = sum_numbers(numbers)

print()
print(f"Los números ingresados son: {numbers}")
print(f"El resultado de la suma de los números ingresados es: {result}")
time.sleep(2)