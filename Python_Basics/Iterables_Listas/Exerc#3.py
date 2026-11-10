import time

print("=================== EJERCICIO DE ITERABLES Y LISTAS ============================")
print("-------------- Intercambie el primer y ultimo elemento -------------------------")
print()

while True:
    mylist = input("Escribe los elementos de la lista separados por comas: ")
    print()

    if "," not in mylist:
        mylist = input("Debes separar los elementos con una coma. Intente de nuevo.")
        print()
        continue

    mylist = [element.strip() for element in mylist.split(",") if element.strip()] # split(",") divide el texto en elementos; strip() elimina los espacios alrededor de cada uno. Si la lista tiene cero o un elemento, queda igual

    if not all(mylist):
        print("No dejes elementos vacíos entre las comas. Intenta de nuevo. \n")
        continue

    break # lista es valida, y saimos del while

if len(mylist) >= 2:
    mylist[0], mylist[-1] = mylist[-1], mylist[0]                               # usando los índices de la lista, el primer elemento está en la posición 0 y el último en la posición -1

print("Lista después del intercambio:", ", ".join(mylist))   # ", ".join(list) muestra las frutas separadas por comas, sin los corchetes

time.sleep(5)