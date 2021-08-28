"""Se pueden crear tupla con () o el contructor tuple"""

tupla1 = (1, 2, 3, 4, 5, 6)
tupla2 = tuple((1, 2, 3, 4, 5, 6))

if tupla1 == tupla2:
    print("La tupla 1 {} es igual a la tupla 2 {}".format(tupla1, tupla2))

"""Las tuplas no se pueden modificar, para modificar se transforman en listas"""
tuplaFrutas = ("Manzana","Pera","Fresa")
tuplaFrutas = list(tuplaFrutas)
tuplaFrutas[0] = "Apple"
tuplaFrutas = tuple(tuplaFrutas)
print(tuplaFrutas)
