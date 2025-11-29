# Ejercicio 4: Ejercicio 4: Manejo de errores
# 1. Modifica el ejercicio 1 para que la edad y altura se pidan en un bucle que repita hasta que se ingrese un número válido.
# 2. Usa try/except para capturar errores si el usuario escribe algo que no sea un número int o float en cada caso.

nombre = input("Introduce tu nombre: ")

for _ in range(10):
    try:
        edad = int(input("Introduce tu edad: "))
        if edad > 0:
            break
        else:
            print("La edad debe ser un número positivo.")
    except ValueError:
        print("Por favor, ingresa un número válido para la edad.")
else:
    edad = 0