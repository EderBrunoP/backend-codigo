# Ejercicio 1
# Solicitar una palabra y validar es está es un palíndromo
# palíndromo -> al derecho y al revés se lee igual

palabra = input("ingrese una palabra: ")

# Solución 1
if palabra == palabra [::-1]:
    print('Es un palidrondomo')
else:
    print('No es un palidrondomo')

# Solución 2
# letras_invertidas = []

# for letra in palabra:
#     letras_invertidas.insert(0,letra)

# palabra_invertida = ''.join(letras_invertidas)

# if palabra == palabra_invertida:
#     print('Es un palindromo')
# else:
#     print('No es un palindromo')

# Solución 3
# palabra_invertida = ''.join(reversed(palabra))
# if palabra == reversed(palabra):
#     print('Es un palíndromo')
# else:
#     print('No es un palíndromo')


# Ejercicio 2
# solicitar el año de nacimiento, este mismo se iterará restándole el año actual
# nos mostrará cuántos años tenemos en cada año iterado

anio_actual=2022
anio_nacimiento=int(input('Ingrese año de nacimiento: '))

if anio_nacimiento < anio_actual:
    edad = anio_actual - anio_nacimiento
    for i in range (edad):
        edad_anterior= i + 1
        if (anio_nacimiento + edad_anterior)==anio_actual:
            print(f'Actualmente en el año {anio_actual}, tienes {edad_anterior} años')
        else:
            print(f'En el año {anio_nacimiento + edad_anterior} tenias {edad_anterior} años ')
else:
    print(f'El año de nacimiento no debe ser mayor a {anio_actual}')



