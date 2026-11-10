import time                 # modulo de Time
print("============================ EJERCICIO #5 ==========================")
print("------------------Cálculo con notas de estudiantes -----------------")
print(" ")                   # imprime una línea en blanco

total_notes = int(input("Ingrese la cantidad de notas a procesar: "))

while total_notes < 1:      # valida que la cantidad de notas debe ser mayor 0
    print("La cantidad de notas a ingresar debe ser mayor a 0")
    total_notes = int(input("Ingrese la cantidad de notas a procesar: "))
    print(" ")             # imprime una línea en blanco

# Definición de variables
approved = int(0)
rejected = int(0)
average = float(0)
average_approved = float(0)
average_rejected = float(0)
note_counter = int(1)

while note_counter <= total_notes:
    actual_note = int(input(f"Ingrese la nota {note_counter}: "))
    average = average + actual_note
    print("")           # imprime una línea en blanco

    if actual_note < 70:
        rejected = rejected + 1
        average_rejected = average_rejected + actual_note

    else:
        approved = approved + 1
        average_approved = average_approved + actual_note

    note_counter = note_counter + 1

note_counter = note_counter - 1

average = average / note_counter

if approved != 0:                       # Valida que exista notas aprobadas
    average_approved = average_approved / approved

if rejected != 0:                       # Validad que exista notas desaprobadas
    average_rejected = average_rejected / rejected

print("")
print(f"El promedio total de notas es de: {average}")
print("")
print(f"La cantidad de notas mayores a 70 es de: {approved}")
print(f"El promedio de notas aprobadas es de: {average_approved}")
print("")
print(f"La cantidad de notas menores a 70 es de: {rejected}")
print(f"El promedio de notas desaprobadas es de: {average_rejected}")
time.sleep(5)




