## function nombre() { logica }

# function en python
# def nombreFunction():
    #pass

# función con parámetro
from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE


def saludar (nombre):
    print(f'Hola {nombre}, como estas?')

saludar ('Eder')


# funcion con parámetros, con valor por defecto
# valores sin parametros van al inicio
def saludarConNombre(nombre,apellido="Bruno"):
    print(f'{nombre} {apellido}')

saludarConNombre("Omar")
saludarConNombre(apellido="Pizarro",nombre="Eder")

# Ejercicio
# crear función que reciba dos números, dónde el primer número tenga 
# tenga un valor por defecto: 10
# si dichos números al sumarlos es par, hallar la mitad
# y si es impar mostrar el resultado de la suma

numero_uno = int(input("Ingrese un número: "))

def suma(numero_uno,numero_dos=10):
    resultado= numero_uno+numero_dos
    if resultado % 2 == 0:
        print(f'El mitad del número {numero_uno} y {numero_dos} es {resultado/2}')
    else:
        print(f'El suma del número {numero_uno} y {numero_dos} es {numero_uno+numero_dos}')

suma(numero_uno)


# Función con multiparametros
# 1er caso: *args -> nombreFuncion("valor1","valor2",...)
# 2do caso: **kwargs -> nombreFuncion(valoruno="1",valordos="2",...)

def alumnosInscritos(*args):
    print(args)

alumnosInscritos("Eder","Omar","Bruno","Pizarro")

#2do caso
def cursosDeAlumnos (**kwargs):
    print(kwargs)

cursosDeAlumnos(curso_uno="Algebra",curso_dos="Aritmetica",curso_tres="Matematica")

# Ejercicio 2
# crea una función que reciba N notas, y te indique
# cuántas desaprobaron y cuántas aprobaron
# nota>10 -> aprobado

def notas(*args):
    aprobados=0
    desaprobados=0
    for nota in args:
        if nota >10:
            aprobados+=1
        else:
            desaprobados+=1
    print (f'El número de notas aprobados es de {aprobados}'
    f'\n El número de notas desaprobadas es de {desaprobados}'
    )
    

notas(15,14,13,11)

