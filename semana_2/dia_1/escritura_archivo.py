from json import loads, dump

## Function open(file,mode)
# file -> el nombre del archivo, tener en cuenta la ubicación física
# mode -> el permiso con el cual va a ser abierto el archivo
## a -> escribe pero mantiene el contenido del archivo
## w -> escribe y reemplaza sobre el contenido del archivo

## Plus +
# r+ -> leer y escribir un archivo

# # Archivo de texto (.txt)
# # file = open('nombres.txt','w')
# file = open('nombres.txt','a')
# # file.write('Eder Bruno')
# file.write('Eder Bruno\n')
# # file.writelines(["Omar Bruno","Omar Pizarro"])
# file.close()

# Archivo json (.json)
# file = open ('alumnos.json','r+')
# file_data=loads(file.read())

# file_data.append({
#     "nombre":"Omar",
#     "edad":28
# })

# file.seek(0) # ubicarnos en la primera fila
# dump(file_data,file,indent=4)

# file.close()

# Contexto with
# _enter_y_exit_
with open('alumnos.json','r+') as file:
    file_data =  loads(file.read())

    file_data.append({
        "nombre":"Yesica",
        "edad":21
    })

    file.seek(0)
    dump(file_data,file,indent=4)

