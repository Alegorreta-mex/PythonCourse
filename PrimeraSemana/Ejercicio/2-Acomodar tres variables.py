a = input("agrega variable 1:")
b = input("agrega variable 2:")
c = input("agrega variable 3:")

if a < b:
    if c < a:
        print(c, a, b)
    elif c < b:
        print(a, c, b)
    else:
        print(a, b, c)
else:
    if a < c:
        print(b, a, c)
    elif b < c:
        print(b, c, a)
    else:
        print(c, b, a)
