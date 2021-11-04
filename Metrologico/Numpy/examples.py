"""import numpy"""
import numpy as np

"""crear un arreglo de 0"""
print("Matrices de zeros")
zeros = np.zeros(shape=(3, 3), dtype=np.uint8)
print(zeros, zeros.dtype)
"""
La funcion zeros crea una matriz numpy de la dimension que se le indica en el primer argumento, el cual acepta un tupple
el segundo argumento es opcional y nos dice que tipo de unidades usa, las mas comunes
np.uint8
np.int8
np.int32
np.int64
float
"""

"""crear un arreglo de 1"""
print("Matrices de unos")
ones = np.ones(shape=(3, 3), dtype=np.int64)
print(ones, ones.dtype)
"""
La funcion crea una matriz de unos y recibe los argumentos parecidos a lo que se indico en la funcion zeros
"""

"""Tambien se puede crear matrices a partir de listas o tuplas, con el metodo array"""
print("Matrices desde Listas")

matriz_listas = np.array(([[11, 21, 31], [12, 22, 32], [13, 23, 33]]))
print(matriz_listas, matriz_listas.dtype)
matriz_tupples = np.array((((11, 21, 31), (12, 22, 32), (13, 23, 33))))
print(matriz_tupples, matriz_tupples.dtype)

"""El metodo array puede inferir el mejor tipo de dato o se le puede forzar a tener uno"""
matriz_intuido = np.array(([[11, 21, 31], [12, 22, 32], [13, 23, 33]]))
matriz_forzado = np.array(([[11, 21, 31], [12, 22, 32], [13, 23, 33]]), dtype=np.float64)
print(matriz_intuido, matriz_intuido.dtype)
print(matriz_forzado, matriz_forzado.dtype)

"""Metodos utiles"""
"""El metodo de shape es muy util para saber las dimensiones de la matriz"""
print("dimensiones", zeros.shape)

"""Funciones utiles"""
"""Para obtener la transpuesta de la matriz es facil con el metodo transposne"""
transpose = np.transpose(matriz_listas)
print("Matriz transpuesta")
print(matriz_listas)
print(transpose)
"""
    El valor que acepta es la matriz a la cual se va a sacar la transpuesta
"""
"""Se puede reacomodar las dimensiones con el metodo reshape"""
print("Matriz Reacomodada")
reshape = np.reshape(matriz_listas, (10))
print(reshape)
"""
    el primer valor es la matriz para reacomodar y el segundo valor es una tupla con la nueva forma
"""
"""se puede calcular el promedio con la funcion mean"""
promedio_c = np.mean(matriz_listas, axis=0)
promedio_r = np.mean(matriz_listas, axis=1)
promedio_t = np.mean(matriz_listas, axis=None)
print("El promedio de la columna es {}, el promedio del renglon es {} y el promedio total es {}".format(promedio_c,
                                                                                                        promedio_r,
                                                                                                        promedio_t))

"""
    Donde el primer argumento es la matriz y el segundo es el eje por el cual se va a sacar el promedio
"""

""" Se tiene una funcion muy parecida para calcular la desviacion estandar usando std"""

desviacion_c = np.std(matriz_listas, axis=0)
desviacion_r = np.std(matriz_listas, axis=1)
desviacion_t = np.std(matriz_listas, axis=None)
print("El desviacion de la columna es {}, el desviacion del renglon es {} y el desviacion total es {}".format(
    desviacion_c,
    desviacion_r,
    desviacion_t))
"""Hay muchos metodos parecidos como min,max,sum,sin,cos,acos"""

"""tambien se puede hacer multiplicaciones por escalares"""
print("Multiplicacion brodcast")
fives = ones * 5
print(fives)

"""o se pueden hacer multiplicaciones de matrices"""
print("Multiplicacion matrices")
A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([[1, 2, 3], [3, 4, 5]])
print(A)
print(B)
producto = np.dot(A, B)
print(producto)

"""o se puede usar el operador @, el cual no lo recomiendo para no confundir cuando se usa para decoradores"""
print(A @ B)

"""o se puede hacer multiplicaciones de producto puntop"""
print("Multiplicacion element wise")
print(fives * (ones * 2))

"""El slicing en arreglos de numpy se hace igual que con listas o tupples en python, con la diferencia que se usa comas para indicar la dimension"""
print("Slicing")
print(matriz_listas)
print("primera renglon")
print(matriz_listas[0, :])
print("ultimo renglon")
print(matriz_listas[-1, :])
print("primera columna")
print(matriz_listas[:, 0])
print("ultima  columna")
print(matriz_listas[:, -1])
print("punto central")
print(matriz_listas[1, 1])
print("los primeros dos datos del primer renglon")
print(matriz_listas[0, -1:-2])
