# Ejercicio 1:
# Solicitar dos números enteros y realizar una calculadora

num_uno =int(input('Ingrese un número entero: '))
num_dos =int(input('Ingrese un número entero: '))
suma = num_uno + num_dos
resta = num_uno - num_dos
multiplicacion = num_uno * num_dos
division = num_uno // num_dos
print (
    f'Calculadora de los números {num_uno} y {num_dos} \n'
    f'suma: {suma} \n'
    f'resta: {resta} \n'
    f'multiplicacion: {multiplicacion} \n'
    f'division: {division} \n'

)

# Ejercicio 2:
# Solicitar un número y validar si es un número par o impar
numero = int(input ('Ingrese un número: '))
print(
    f'Par: {numero%2==0} \n'
    f'Impar: {numero%2!=0}'
    )




