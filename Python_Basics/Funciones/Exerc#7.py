print("============================== EJERCICIO DE FUNCIONES ================================")
print("-----------------------------------Ejercicio #7---------------------------------------")
print()

import time


def get_numbers():
    while True:
        text = input("Ingrese números enteros separados por comas: ")
        parts = text.split(',')
        numbers = []

        try:
            for part in parts:
                number = int(part.strip())
                numbers.append(number)

            return numbers

        except ValueError:
            print(
                "Error: Asegúrese de ingresar solo números "
                "enteros separados por comas."
            )


def is_prime(number):
    if number < 2:
        return False

    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            return False

        divisor += 1

    return True


def get_prime_numbers(numbers):
    prime_numbers = []

    for number in numbers:
        if is_prime(number) and number not in prime_numbers:
            prime_numbers.append(number)

    return prime_numbers


user_numbers = get_numbers()
prime_numbers = get_prime_numbers(user_numbers)

print()
print(f"Números ingresados: {user_numbers}")
print(f"Números primos encontrados: {prime_numbers}")

time.sleep(2)