class User:
    def __init__(self, name, age):
        """Constructor para inicializar los datos del usuario"""
        self.name = name
        self.age = age
        print(f"Usuario {self.name} de {self.age} años registrado correctamente.")

    def display_user(self):
        """Método para mostrar los datos del usuario"""
        print(f"Nombre: {self.name}, Edad: {self.age}")

    def __del__(self):
        """Destructor para simular la limpieza de recursos"""
        print(f"Datos del usuario {self.name} eliminados y recursos liberados.")

# Solicitar datos al usuario
name = input("Ingrese su nombre: ")
age = int(input("Ingrese su edad: "))

# Crear objeto de la clase User
user = User(name, age)

# Mostrar los datos del usuario
user.display_user()

# Destruir el objeto explícitamente
del user

# Intentar acceder a los atributos después de destruir el objeto
try:
    print(user.name)  # Esto debería generar un error si el objeto ha sido destruido
except NameError as e:
    print(f"Error: {e} - El objeto ha sido eliminado y los datos ya no están disponibles.")
