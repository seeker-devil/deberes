# Clase base (Madre)
class Madre:
    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo privado

    # Método getter para acceder al nombre (Encapsulación)
    def get_nombre(self):
        return self.__nombre

    # Método polimórfico
    def saludar(self):
        return "Hola, soy la madre."

# Clase derivada (Hijo) que hereda de Madre
class Hijo(Madre):
    def saludar(self):
        return "Hola, soy el hijo."  # Herencia

# Se define nombres de madre e hijo
madre = Madre("Ana")
hijo = Hijo("Carlos")

# Uso de métodos
print(madre.get_nombre())  # Acceso al atributo con getter (Encapsulación)
print(madre.saludar())  

print(hijo.get_nombre())  # Acceso al atributo con getter (Encapsulación)
print(hijo.saludar())  # Polimorfismo
