def saludar(nombre):
    return f"¡Hola, {nombre}! Bienvenido/a al taller de Git."
nombre = input("¿Cómo te llamás? ")
print(saludar(nombre))
anio = int(input("¿En qué año naciste? "))
print(f"Este año cumplís {2026 - anio} años.")