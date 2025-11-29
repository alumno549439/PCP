# Ejercicio 3: Parámetros con valores por defecto y *args

# 1. Crea una función presentar_persona(nombre="Usuario", edad=None, *aficiones) que muestre un mensaje como:
def presentar_persona(nombre="Usuario", edad=None, *aficiones):
    return f"{nombre} tiene {edad} años y le gusta: {aficiones}"

# 2. Prueba la función con diferentes números de aficiones.
presentar_persona("Olivia", 25, "leer", "correr", "viajar")
presentar_persona("Guille", 31, "tocar la guitarra", "hacer deporte", "dormir", "cantar", "bailar")
presentar_persona("Alexia", 22, "escuchar musica")

# 3. Dale un valor por defecto al parámetro nombre para cuando no se pase ninguno.
def presentar_personas(nombre="Andrea", edad=None, *aficiones):
    return f"{nombre} tiene {edad} años y le gusta: {aficiones}"
presentar_personas(22, "escuchar musica")