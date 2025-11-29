from tarea4 import temp

temperatura = float(input("Introduce un valor (en ºC): "))
listaTemperaturas = []
listaTemperaturas.append(temperatura)

confirm = input("¿Desea incluir algún valor más? (En caso afirmativo escriba 'SI', en caso negativo escriba 'NO'): ")
while confirm == 'SI':
    temperatura = float(input("Introduce un valor (en ºC): "))
    listaTemperaturas.append(temperatura)
    temp(listaTemperaturas)

    confirm = input("¿Desea incluir algún valor más? (En caso afirmativo escriba 'SI', en caso negativo escriba 'NO'): ")
    if confirm == 'NO':
        break