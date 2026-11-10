import time

print("=================== EJERCICIO DE ITERABLES Y LISTAS ============================")
print("-------------- Intercambie el primer y ultimo elemento -------------------------")
print()

while True:
    list = input("Escribe los elementos de la lista separados por comas: ")
    print()

    if "," not in list:
        list = input("Debes separar los elementos con una coma. Intente de nuevo.")
        print()
        continue

    list = [element.strip() for element in list.split(",") if element.strip()] # split(",") divide el texto en elementos; strip() elimina los espacios alrededor de cada uno. Si la lista tiene cero o un elemento, queda igual

    if not all(list):
        print("No dejes elementos vacíos entre las comas. Intenta de nuevo. \n")
        continue

    break # lista es valida, y saimos del while

if len(list) >= 2:
    list[0], list[-1] = list[-1], list[0]                               # usando los índices de la lista, el primer elemento está en la posición 0 y el último en la posición -1

print("Lista después del intercambio:", ", ".join(list))   # ", ".join(list) muestra las frutas separadas por comas, sin los corchetes

time.sleep(5)