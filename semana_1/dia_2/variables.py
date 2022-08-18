## Las variables solo pueden ser nombradas con letrs, no alfanumericcas ni numericos
### Formato: snakecase
# nombre_de_variable
# no utilizar nombres de variable reservadas, para el uso general
## main


# variables de texto

nombre="Eder"
apellidos="Bruno"
texto="""
Buenos días:
    La carta redactada...
    ..........
"""

texto_en_linea=(
    "Hola, como estas"
    "Estoy en clases de backend"
)

# # Operador de Salida 
# print(nombre)
# print(texto)
# print(texto_en_linea)

# variables númericos
numero_entero=10
numero_decimal=10.50

# #concatenacion
# print(nombre + " "+apellidos )
# print(nombre, apellidos)
# # f-string
# print(f"{nombre} {apellidos}")

#dinamismo
# type -> nos va a retornar el tipo de variable

# print(type(nombre))


# nombre=1500
# print(type(nombre))

# function nombre() ->salida
# function nombre_completo(nombre, apellido) -> str { return ´${nombre} ${apellido}´}

#variables booleanas
# true y false -> 1 y 0
verdadero=True
falso = False

#definimos una variable con valor nulo
# null
variable_nulo = None

## Asignación múltiple
# persona = "Juan"
# nacionalidad = "peruano"
persona, nacionalidad ="Juan","Peruano"
print (persona,nacionalidad)


