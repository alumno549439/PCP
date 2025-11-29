def temp(listaTemperaturas):
    listaTemperaturas.sort()
    print(listaTemperaturas)
    
    min = listaTemperaturas[0]
    max = listaTemperaturas[-1]
    mean = round(sum(listaTemperaturas)/len(listaTemperaturas),1)
    print("En la lista de temperaturas...\n"
      f"- La temperatura mínima es {min}ºC\n"
      f"- La temperatura máxima es {max}ºC\n"
      f"- La temperatura media es {mean}ºC")