# clase 
# Abstracción -  Polimorfismo


class Mueble:
    precio = 0.00
    tipo =""
    color=""

    # Método de instancia
    def indicarTipo(self):
        print(f'El tipo es {self.tipo}')

sofa_cama = Mueble()
sofa_cama.tipo="Sofa cama"
# sofa_cama.indicarTipo()

silla = Mueble()
silla.tipo="Silla"
# silla.indicarTipo()

# Clase con constructor
# constructor() -> _init_
class Persona():
    def __init__(self,nro_documento,nombres,apellidos,edad=0):
        self.nro_documento= nro_documento
        self.nombres= nombres
        self.apellidos= apellidos
        self.edad= edad

# eder=Persona("12345678","Eder","Bruno")
# print(eder.nombres)

# ------------------
class Usuario():
    def __init__(self,usuario,contrasenia):
        self.usuario = usuario
        self.__contrasenia=contrasenia
        self.contrasenia=self.__encriptarContrasenia()

    # Encapsulamiento
    # Propiedades ocultas o metodos ocultos (__)
    
    def __encriptarContrasenia(self):
        return f'vvsssd{self.__contrasenia}q2323w""#2!"'

    def mostrarContrasenia(self):
        print(self.__contrasenia)

usuario_uno = Usuario("eder","1234")
# print(usuario_uno.contrasenia)
# print(usuario_uno.mostrarContrasenia())

# Getters y Setters
class Animal:
    def __init__(self,nombre,raza,color) :
        self.nombre=nombre
        self.raza=raza
        self.color=color
        self.__duenio=""

    # # Primera forma
    # def __getDuenio(self):
    #     return self.__duenio
    
    # def __setDuenio(self,duenio):
    #     self.__duenio = duenio

    # duenio=property(__getDuenio,__setDuenio)

    # segunda forma
    # Getter
    @property #decorador
    def duenio(self):
        return self.__duenio
    
    # Setter
    @duenio.setter
    def duenio(self,duenio):
        self.__duenio = duenio

perro= Animal("Dino","Frenchie","Vaquita")
perro.duenio="Eder"
print(perro.duenio)
