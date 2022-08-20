# Crear un programa que permita ingresar 6 numeros
# de los cuales si uno tiene un formato incorrecto, nos va indicar un mensaje de error
# pero los que si tengan el formato correcto, se agregarán en una lista
# al final nos retornara la lista con los números correctos

numeros=[]

# si no utilizamos una variable colocar un _

for _ in range (6):
    try:
        numero  = int(input("Ingresa el número: "))
        numeros.append(numero)
    except Exception:
        print('El número ingresado es incorrecto')

print(numeros)