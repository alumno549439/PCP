# Ejercicio 1: Tipos de datos y entrada de usuario
# 1. Pide al usuario su nombre, edad y altura en metros.
nombre = str(input ("Introduce tu nombre: "))
edad = int(input ("Introduce tu edad: "))
altura = float(input ("Introduce tu altura: "))

# 2. Muestra un mensaje usando f-string con los datos ingresados.
print(f"Hola {nombre}, tienes {edad} años y mides {altura} metros.")

# 3. Muestra el tipo de dato de cada variable.
print("Nombre:" , type(nombre) ,"\nEdad:", type(edad) ,"\nAltura:" , type(altura))