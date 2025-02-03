import math

# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)  # Fórmula del área de un círculo
    return area

# Solicitar al usuario el radio
radio_input = input("Introduce el radio del círculo en metros: ")
radio = float(radio_input)  # Convertir la entrada a float

# Calcular el área
area_circulo = calcular_area_circulo(radio)

# Mostrar el resultado
print(f"El área del círculo con radio {radio} metros es: {area_circulo:.2f} metros cuadrados.")
