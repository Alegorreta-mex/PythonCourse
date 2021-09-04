#el siguiente codigo es un ciclo for con un if adentro , verificando si el numero es 3, al encontrarlo rompe el ciclo

for i in range(5):
    print(i)
    if i == 3:
        print("fin por encontrar valor")
        break
else:
    print("fin por acabar ciclo")

#este for termina normal y popr lo tanto vemos que se escribe en el else
for i in range(5):
    print(i)
else:
    print("fin por acabar ciclo")

#este for si encuentra un numero par continua al siguiente numero
for i in range(5):
    if i % 2 == 0:
        print("{} es par".format(i))
    elif i % 2 != 0:
        print("{} es impar".format(i))