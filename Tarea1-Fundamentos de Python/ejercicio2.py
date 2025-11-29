# Ejercicio 2: Funciones básicas

from ejercicio1 import nombre,altura

# 1. Crea una función saludar(nombre) que reciba un nombre y devuelva un saludo:
def saludar(nombre):
    return f"Hola, {nombre}"

# 2. Crea una función calcular_imc(peso, altura) que devuelva el IMC usando la fórmula:
def calcular_imc(peso, altura):
    imc = round(float(peso) / float(altura) ** 2,2) # ,2 --> redondea a dos decimales
    return imc

# 3. Llama a estas funciones con los datos ingresados en el ejercicio 1 y muestra los resultados.
print(saludar(nombre))

peso = input("Introduce tu peso en Kg: ")
resultado = calcular_imc(peso, altura)
print(f"Tu IMC es: {resultado:.2f}") # Se utiliza .2f por los float