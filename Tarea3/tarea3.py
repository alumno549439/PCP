import sys

'''
Definir variable para número
Pedir usuario introduzca un número
Validar que el usuario solo introduce valor del 1 al 10
Imprimir el número multiplicado por un rango del 1 al 10 y el resultado

'''
global num              # Creamos una variable

def pintarTablas(numero):
    for i in range(10):
        print(f"{numero} x {i} = {numero*{i}}")

def pedirNumero():
    global num          # Es la misma variable, pero vamos a modificar su valor
    while num < 1 or num > 10:
        print("Los valores válidos son del 1 al 10")
        try:
            num = int (input("¿Qué tabla de multiplicar quieres?: "))
        except ValueError:
            print("Solo valores del 1 al 10")
        except:
            print("Se ha producido un error")

def ejecutarConArgumento():
    if len(sys.argv) < 1 and len(sys.argv) > 1:
        print("El programa solo recibe un argumento")
    else:
        pintarTablas(int(sys.argv[1]))