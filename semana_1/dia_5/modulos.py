from camelcase import CamelCase as ClaseCamel

instancia = ClaseCamel()
texto = "hola Eder"
print(instancia.hump(texto))