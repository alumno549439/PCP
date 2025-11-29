"""
En este primer programa, vamos a
practicar la sintaxis básica de Python

"""
# Esto imprime "hola mundo" en pantalla:
print("Hola Mundo")

print(type(10)) # Esto imprime el tipo de dato que es el 10

edad = 25
precio = 19.90
nombre = "Python"
activo = True
ventas = None

print("Edad",type(edad),"Precio",type(precio))

lista1 = [20, 30, 40, 50] # Una lista siempre empieza por el índice 0
print(lista1[1]) # Muestra el índice 1 de la lista




midiccionario = {
    "nombre" : "Paquito",
    "apellido":"Chocolatero",
    "usuario":"chocopaquito",
    "contraseña":"1234"
}
print(midiccionario["nombre"])

conjunto2 = {1, 2, 2, 3, "hola", "adios"}
print(list(conjunto2)[2])

numero1 = int(input ("Introduce el primer número:"))    # Sin el int lo tomaría como cadena y no se sumaría, se juntarían
numero2 = int(input ("Introduce el segundo número:")) 
print(numero1 + numero2)


if numero1 > numero2:
    print(numero2 + " es mayor que " + numero1)
elif numero1 < numero2:
    print(numero1 + " es mayor que " + numero2)
else:
    print(numero1 , "y" , numero2 , " son iguales")


for elemento in lista1:
        print(elemento)

for i in range(5):
        print(i)




try:
    # Código que puede lanzar una excepción
    resultado = 10 / 2
except ZeroDivisionError:
    # Código a ejecutar si se produce una excepción del tipo ZeroDivisionError
    print("No se puede dividir por cero.")
except ValueError:
     print("No se puede dividir por algo que no sea un número")
else:
    # Código a ejecutar si no se produce ninguna excepción
    print("La división fue exitosa. El resultado es:", resultado)
finally:
    # Código a ejecutar siempre, independientemente de si se produce una excepción o no
    print("Esta línea se ejecutará siempre.")

def sumar(a, b):
  suma = a + b
  return suma   # Devuelve la suma de a y b

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
print(sumar(numero1, numero2))