"""Se pueden crear listas con [] o el contructor list"""

list1 = [1, 2, 3, 4, 5, 6]
list2 = list((1, 2, 3, 4, 5, 6))

if list1 == list2:
    print("La lista 1 {} es igual a la lista 2 {}".format(list1, list2))

listaFrutas = ["manzana", "pera", "durazno"]

"""Para accedar a un item se usa [] despues del nombre de la lista y su posicion, recordemos que empieza en el 0"""
print("La fruta con la primera posicion es {}".format(listaFrutas[0]))
print("La fruta con la segunda posicion es {}".format(listaFrutas[1]))

"""Para agregar un elemento a la lista se puede user la funcion insert o append"""
"""append se ingresa al final"""
listaFrutas.append("fresa")

"""insert la agrega en la posicion indicada y recorre a la derecha"""
listaFrutas.insert(1, "piña")

print("La nueva lista es {}".format(listaFrutas))

"""Para modificar basta con igualar el elemento de la lista"""
listaFrutas[0] = "Apple"
print("La nueva lista es {}".format(listaFrutas))

"""Para eliminar un elemento de la lista se puede usar pop or remove"""
listaFrutas.remove("durazno")
print("La nueva lista es {}".format(listaFrutas))
listaFrutas.pop(1)
print("La nueva lista es {}".format(listaFrutas))

"""Para limpiar la lista usamos el funcion clear"""
listaFrutas.clear()
print("La nueva lista es {}".format(listaFrutas))

"""Para eliminar la lista usamos el funcion del"""
del listaFrutas
print("La nueva lista es {}".format(listaFrutas))