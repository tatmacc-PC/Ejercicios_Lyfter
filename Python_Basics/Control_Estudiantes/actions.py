# Define subject keys and their display names.
SUBJECTS = {
    "spanish": "Español",
    "english": "Inglés",
    "social_studies": "Sociales",
    "science": "Ciencias",
}


def normalize_name(name):
    # Remove extra spaces and ignore case when comparing names.
    return " ".join(name.split()).casefold()


def is_valid_name(name):
    # Reject empty names.
    if not name.strip():
        return False

    # Allow only letters and spaces.
    for character in name:
        if not character.isalpha() and not character.isspace():
            return False

    return True


def is_valid_section(section):
    # Accept one or two digits followed by an uppercase letter.
    if len(section) not in (2, 3):
        return False

    number = section[:-1]
    letter = section[-1]

    # Reject sections starting with zero.
    if number[0] == "0":
        return False

    # Validate the numeric part.
    for character in number:
        if character not in "0123456789":
            return False

    return letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def student_exists(students, name, section):
    # Match students using both name and section.
    for student in students:
        same_name = (
            normalize_name(student["name"])
            == normalize_name(name)
        )

        same_section = (
            student["section"].strip().upper()
            == section.strip().upper()
        )

        if same_name and same_section:
            return True

    return False


def get_valid_name():
    # Repeat until a valid name is entered.
    while True:
        name = input("Nombre completo: ").strip()

        if is_valid_name(name):
            return " ".join(name.split())

        print("Ingrese un nombre que contenga solo letras y espacios.")


def get_valid_section():
    # Normalize the section before validating it.
    while True:
        section = input("Sección: ").strip().upper()

        if is_valid_section(section):
            return section

        print("Sección inválida. Ejemplos válidos: 7A, 10A, 11B.")


def get_valid_grade(subject):
    # Repeat until a numeric grade between 0 and 100 is entered.
    while True:
        try:
            grade = float(input(f"Nota de {subject}: "))

            if 0 <= grade <= 100:
                return grade

            print("La nota debe estar entre 0 y 100.")

        except ValueError:
            print("Ingrese un número. Use punto para los decimales.")


def get_valid_quantity():
    # Require a positive integer.
    while True:
        try:
            quantity = int(
                input("¿Cuántos estudiantes desea ingresar? ")
            )

            if quantity > 0:
                return quantity

            print("La cantidad debe ser mayor que cero.")

        except ValueError:
            print("Ingrese un número entero.")


def confirm_action(message):
    # Require an explicit yes or no answer.
    while True:
        answer = input(f"{message} (s/n): ").strip().casefold()

        if answer in ("s", "si", "sí"):
            return True

        if answer in ("n", "no"):
            return False

        print("Respuesta inválida. Ingrese s o n.")


def add_student(students):
    # Validate the student's identity and prevent duplicates.
    while True:
        name = get_valid_name()
        section = get_valid_section()

        if not student_exists(students, name, section):
            break

        print("Ya existe un estudiante con ese nombre y sección.")
        print("Ingrese nuevamente los datos.")

    student = {
        "name": name,
        "section": section,
    }

    # Request a valid grade for every subject.
    for subject_key, subject_name in SUBJECTS.items():
        student[subject_key] = get_valid_grade(subject_name)

    students.append(student)
    print("Estudiante registrado correctamente.")


def add_students(students):
    quantity = get_valid_quantity()

    # Register students one at a time.
    for index in range(quantity):
        print(f"\n--- Estudiante {index + 1} de {quantity} ---")
        add_student(students)


def calculate_average(student):
    # Calculate the average of the four subject grades.
    total = 0

    for subject_key in SUBJECTS:
        total += student[subject_key]

    return total / len(SUBJECTS)


def show_student(student):
    # Display one student's information.
    print(f"\nNombre: {student['name']}")
    print(f"Sección: {student['section']}")

    for subject_key, subject_name in SUBJECTS.items():
        print(f"{subject_name}: {student[subject_key]:.2f}")

    print(f"Promedio: {calculate_average(student):.2f}")


def show_students(students):
    if not students:
        print("No hay estudiantes registrados.")
        return

    for student in students:
        show_student(student)


def show_top_three(students):
    if not students:
        print("No hay estudiantes registrados.")
        return

    # Sort a new list from highest to lowest average.
    sorted_students = sorted(
        students,
        key=calculate_average,
        reverse=True,
    )

    print("\n--- TOP 3 DE ESTUDIANTES ---")

    # Display up to three students.
    for position, student in enumerate(sorted_students[:3], start=1):
        print(f"\nPuesto #{position}")
        show_student(student)


def show_general_average(students):
    # Avoid division by zero.
    if not students:
        print("No hay estudiantes registrados.")
        return

    total = 0

    for student in students:
        total += calculate_average(student)

    general_average = total / len(students)

    print(f"\nPromedio general: {general_average:.2f}")


def delete_student(students):
    if not students:
        print("No hay estudiantes registrados.")
        return

    print("\n--- ELIMINAR ESTUDIANTE ---")
    name = get_valid_name()
    section = get_valid_section()

    for student in students:
        same_name = (
            normalize_name(student["name"])
            == normalize_name(name)
        )
        same_section = student["section"] == section

        if same_name and same_section:
            show_student(student)

            # Delete only after user confirmation.
            if confirm_action("¿Desea eliminar este estudiante?"):
                students.remove(student)
                print("Estudiante eliminado correctamente.")
            else:
                print("Eliminación cancelada.")

            return

    print("No existe un estudiante con ese nombre y sección.")


def show_failed_students(students):
    if not students:
        print("No hay estudiantes registrados.")
        return

    print("\n--- ESTUDIANTES REPROBADOS ---")
    found_failed_student = False

    for student in students:
        failed_subjects = []

        # Collect subjects with grades below 60.
        for subject_key, subject_name in SUBJECTS.items():
            grade = student[subject_key]

            if grade < 60:
                failed_subjects.append((subject_name, grade))

        if failed_subjects:
            found_failed_student = True

            print(f"\nNombre: {student['name']}")
            print(f"Sección: {student['section']}")
            print("Materias reprobadas:")

            for subject_name, grade in failed_subjects:
                print(f"- {subject_name}: {grade:.2f}")

    if not found_failed_student:
        print("No hay estudiantes con materias reprobadas.")