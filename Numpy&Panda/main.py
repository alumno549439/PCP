# -------------------- NUMPY ---------------------
import numpy as np
print (np.__version__)

# Array de una dimensión
a = np.array([1,2,3,4,5])
print(a)

# Array de dos o más dimensiones
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)

# zeros(): Genera un array de ceros del tamaño que le indiquemos
c = np.zeros(5)
print(c)

# ones(): Genera un array de unos del tamaño que le indiquemos
d = np.ones(5)
print(d)

# arange(): Genera un array entre dos valores indicados y a intervalos específicos (algo como range())
e = np.arange(0,10)
print(e)

# linspace(): Genera un array entre dos valores y con un tamaño indicado, compuesto por valores equidistantes entre cada elemento
f = np.linspace(0, 2, 5)
print(f)

# eye(): Genera una matriz identidad del tamaño indicado:
g = np.eye(5)
print(g)

# random.rand(): Genera un array del tamaño inficado, con valores aleatorios entre 0 y 1
h = np.random.rand(5)
print(h)




# -------------------- PANDAS ---------------------
import pandas as pd

serie1 = pd.Series([1,2,3])
serie1.name = "primeros"
print(serie1)

df1 = pd.DataFrame({"columna1":[3,2,5,4,1], "columna2":["a","b","c","d","e"], "columna3":["?","!","#","@","&"]})
print(df1)

# Crear un DataFrame a partir de un fichero CSV (buscado en Google: )
df2 = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")
print(df2.head())

# Ver cuántos elementos tiene nuestro DataFrame
print(df2.size)

# Ver cuántos 
print(df2.shape)

# Ver X elementos desde el inicio del CSV
print(df2.head(5))

# Ver X elementos desde el final del CSV
print(df2.tail(5))

# Podemos persobalizar los nombres de las columnas
df1.columns = ["largo_sepalo","ancho_sepalo","largo_petalo","ancho_petalo","especie"]
print(df2.head())

# Devuelve los identificadores de columna de nuestro dataframe
print(df2.iloc)

# .describe(): Muestra estadísticas genéricas
print(df2.describe())


print(df2["sepal_width"].value_counts())

# Muestra los tipos de datos por columns
print(df2.dtypes)

# Muestra lo que ocupa nuestro DataFrame
print(df2.memory_usage().sum())/1024

# 
print(df2.T.head())

# Altera el orden de salida en la columna que le pidas
print(df1.sort_values("columna1", ascending=False)) # Por defecto está en orden ascendente, podemos cambiarlo con ascending

# Podemos especificar una serie de columnas y filas concretas
print(df1.iloc[[1,4],[1,2]])

# Especificar varias columnas por sus identificadores
print(df1[["columna1", "columna3"]])

# Ver columnas que contengan cierto valor específico
print(df1[df1["columna1"]>2])


print(df1.columna1[3])

