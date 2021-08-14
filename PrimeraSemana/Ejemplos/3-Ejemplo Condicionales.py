a = 200
b = 300
c = 400

# verificamos cual de los dos numeros es el matoy
if a > b:
    print("el valor de a es mayor al valor de b")
else:
    print("el valor de b es mayor al valor de a")

# verificamos si a b es un valor entre a y c
if a <= b and b <= c:
    print("b es un numero entre a y c")
else:
    print("b no es un valor entre a y c")

# verificamos si b es menor a a y si no checamos si es menor a c

if b < a:
    print("b es menor a a")
elif b < c:
    print("b es menor a c pero no a a")


