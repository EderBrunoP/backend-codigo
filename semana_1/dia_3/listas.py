# Mutable
#Nos ayuda a almacenar mas de un valor
# se utiliza corchetes

# persona_uno = "Carlos"
# persona_dos = "Luis"
# persona_tres ="Cesar"

# Forma correcta
personas = ["Carlos", "Luis","Cesar"]
# n-1

print (personas)
print (personas[2])

# Funciones
# append -> agregar un valor al final de una lista
personas.append("Eder")
print (f'append -> {personas}')

# insert -> agrega un valor en una lista, según la posición o índice mencionado
personas.insert(0,"David")
print (f'append -> {personas}')

# index -> retorna el indice del valor mencionado
indice_luis = personas.index("Luis")
print (f'index luis -> {indice_luis}')

# extend -> unir dos listas
personas_nuevas = ["Andres","Daniel","Arturo"]
personas.extend (personas_nuevas)
print (f'extend -> {personas}')

#remove -> eliminar un valor de una lista
personas.remove("Eder")
print (f'remove -> -> {personas}')

# pop -> eliminar un valor según la posición o el índice
personas.pop(3)
print (f'pop -> {personas}')

# sort -> ordenar los valores de una lista,por defecto lo ordena de mayor a menor
#reverse = False -> menor a mayor
#reverse = True -> mayor a menor
personas.sort(reverse=True) 
print (f'sort -> {personas}')

# count -> retorna las veces que existe un elemento
personas.append("Daniel")
daniel_contador=personas.count("Daniel")
print (f'count -> {daniel_contador}')

# Len -> cuenta los elementos de una estructura de datos | Length
print (f'Total de personas -> {len(personas)}')


