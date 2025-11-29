# import operaciones
from operaciones import resta
# también podemos ponerle un alias a lo importado: from operaciones import resta as restar


numero1 = int(input ("Introduce el primer número:"))
numero2 = int(input ("Introduce el segundo número:"))
print(resta(numero1,numero2))