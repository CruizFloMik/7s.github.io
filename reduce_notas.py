# **Cálculo del promedio de las notas de los estudiantes utilizando la función reduce()**

# La función reduce() nos permite aplicar una función iterativamente a los elementos de una secuencia,
#produciendo un único valor como resultado.

# En este ejemplo, la función reduce() se usa para calcular el promedio de las notas de los estudiantes.
#La función lambda() que se pasa a la función reduce() suma los dos primeros elementos de la secuencia 
#y devuelve el resultado.


import random

# Importamos la función reduce()
from functools import reduce

# Definimos una función lambda para sumar dos números
sumar = lambda x, y: x + y

# Generamos una lista con las notas de los estudiantes
notas = [random.randint(0, 10) for i in range(100)]

# Calculamos el promedio de las notas
promedio = reduce(sumar, notas) / len(notas)

# Imprimimos el promedio
print(f"El promedio de las notas es: {promedio}")
