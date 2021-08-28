"""Se pueden crear sets con {} o el contructor set"""

set1 = {1, 2, 3, 4, 5, 6}
set2 = set((1, 2, 3, 4, 5, 6))

if set1 == set2:
    print("La set 1 {} es igual a la set 2 {}".format(set1, set2))

"""Los set no permiten duplicados"""
setduplicados = {1, 1, 1, 1, 2, 2, 3, 2}
print("Los set no permiten duplicados {}".format(setduplicados))

"""Los sets se utiluzan para operaciones de conjuntos"""

conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

print("La union de los conjuntos es {}".format(conjunto1.union(conjunto2)))
print("La interseccion de los conjuntos es {}".format(conjunto1.intersection(conjunto2)))
print("La diferencia del conjunto 1 al conjunto 2 es {}".format(conjunto1.difference(conjunto2)))