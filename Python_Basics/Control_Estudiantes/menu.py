import os

import actions
import data


def clear_screen():
    # Clear the terminal on Windows, macOS, or Linux.
    os.system("cls" if os.name == "nt" else "clear")


def wait_for_main_menu():
    # Wait until the user enters zero to return to the main menu.
    while True:
        option = input(
            "\nIngrese 0 para regresar al menú principal: "
        ).strip()

        if option == "0":
            return

        print("Opción inválida. Ingrese 0 para regresar.")


def run_menu(students):
    clear_screen()

    # Keep displaying the menu until the user chooses to exit.
    while True:
        print("--- SISTEMA DE ESTUDIANTES ---")
        print("1. Ingresar estudiantes")
        print("2. Ver todos los estudiantes")
        print("3. Ver top 3 de estudiantes")
        print("4. Ver promedio general")
        print("5. Exportar datos a CSV")
        print("6. Importar datos desde CSV")
        print("7. Eliminar estudiante")
        print("8. Ver estudiantes reprobados")
        print("9. Salir")

        option = input("\nSeleccione una opción: ").strip()

        # Validate the selection before clearing the screen.
        if option not in (
            "1", "2", "3", "4", "5", "6", "7", "8", "9"
        ):
            print("Opción inválida. Ingrese un número del 1 al 9.")
            wait_for_main_menu()
            clear_screen()
            continue

        # Clear the menu before displaying the selected action.
        clear_screen()

        if option == "1":
            actions.add_students(students)

        elif option == "2":
            actions.show_students(students)

        elif option == "3":
            actions.show_top_three(students)

        elif option == "4":
            actions.show_general_average(students)

        elif option == "5":
            data.export_students(students)

        elif option == "6":
            data.import_students(students)

        elif option == "7":
            actions.delete_student(students)

        elif option == "8":
            actions.show_failed_students(students)

        elif option == "9":
            print("Hasta luego.")
            break

        # Keep the results visible until the user enters zero.
        wait_for_main_menu()
        clear_screen()