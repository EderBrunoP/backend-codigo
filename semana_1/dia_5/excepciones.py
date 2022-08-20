try:
    numero = int(input("Ingrese un número: "))
    resultado =10 / numero
    print(resultado)
except ValueError:
    print('El valor ingresado no es un número')
except ZeroDivisionError:
    print('El número ingresado debe ser mayor a 0')
except KeyboardInterrupt:
    print('\n La aplicación se cerró')
# la sgte línea nos permitirá detectar errores
except Exception as e:
    print(e.__class__) #saber que clase de error es
    print('Hay un error')
else: # se va ejecutar siempre y cuando no haya un error
    print(f'No hubo error -> {resultado}')
finally: # siempre se ejecutará exista o no un error
    print(f'Siempre ')


