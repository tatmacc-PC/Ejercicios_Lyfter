def add_numbers(current, num1):
    return current + num1


def substract_numbers(current, num1):
    return current - num1


def multiply_numbers(current, num1):
    return current * num1


def divide_numbers(current, num1):
    try:
        return current / num1
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
        return None


def clear_result():
    return 0


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")


def main():
    print("======================== EJERCICIO EXCEPCIONES ======================================")
    print("--------------------------------Ejercicio #1-----------------------------------------")
    print()

    import time

    # Variable local: pertenece únicamente a main().
    current_number = get_number("Ingrese un número actual: ")

    while True:
        print(f"\nNúmero actual: {current_number}")
        print("Seleccione una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Limpiar resultado")
        print("6. Salir")

        choice = input(
            "Ingrese el número de la operación que desea realizar: "
        ).strip()

        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            continue

        if choice == '6':
            print("Saliendo del programa...")
            break

        if choice == '5':
            current_number = clear_result()
            print("Resultado limpiado. El número actual es ahora 0.")
            continue

        num1 = get_number("Ingrese el segundo número: ")

        if choice == '1':
            current_number = add_numbers(current_number, num1)

        elif choice == '2':
            current_number = substract_numbers(current_number, num1)

        elif choice == '3':
            current_number = multiply_numbers(current_number, num1)

        elif choice == '4':
            result = divide_numbers(current_number, num1)

            if result is not None:
                current_number = result

        print()
        print(f"Resultado actual: {current_number}")

        time.sleep(1)


if __name__ == "__main__":
    main()