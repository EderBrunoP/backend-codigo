# Diccionario
# {key:value}

persona = {
    "nombres":"José",
    "apellidos":"Velarde",
    "especialidades":[
        {
            "nombre":"Frontend"
        },
        {
            "nombre":"Backend"
        }
    ],
}

print (f'obtener el nombre -> {persona["nombres"]} ') #personas.nombres
print (f'obtener la segunda especialidad -> {persona["especialidades"][1]["nombre"]} ')

# items -> retorna una lista de tuplas (clave, valor)
print(f'items  -> {persona.items()}')

# keys -> retorna una lista con todas las claves
print(f'keys -> {persona.keys()}')

# values -> retorna una lista con todos los valores
print(f'values -> {persona.values()}')

# Agregar nueva clave - valor
persona['edad']=25

# get -> busca la clave en mención, sino la encuentra retorna None
print(f'get -> {persona.get("edad")}')

# pop -> eliminar una clave con su valor
persona.pop("especialidades")
print(f'pop -> {persona}')

# update -> actualizar un diccionario
persona.update({"hobbies":["jugar partido"]})
print(f'update -> {persona}')

