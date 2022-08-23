## Function open(file,mode)
# file -> el nombre del archivo, tener en cuenta la ubicación física
# mode -> el permiso con el cual va a ser abierto el archivo
## r -> lectura
## a -> 
## w -> escritura
## x -> creación, crea el archivo si este no archivo, si exsite retornara error

# open('nombres.txt','x') // ejemplo de crear archivo

file = open('prueba.txt','r')
print (file)

# Al abrir un archivo en modo lectura, tenemos 2 funciones
# read() -> retornamos el contenido del archivo
# readlines() -> retornamos
# file.seek(0) -> esta función nos regresa al cursor inicial

for line in file:
    print(line)

