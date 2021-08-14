# declaracion int
x = 1
print("x con valor {} es del tipo {}".format(x, type(x)))

# declaracion float
y = .5
print("y con valor {} es del tipo {}".format(y, type(y)))

# declaracion str
z = "5.5"
print("z con valor {} es del tipo {}".format(z, type(z)))

# se puede cambiar el tipo de dato pero puede traer perdida de informacion
z_to_float = float(z)
print("z con valor {} es del tipo {}".format(z_to_float, type(z_to_float)))
z_to_int = int(z_to_float)
print("z con valor {} es del tipo {}".format(z_to_int, type(z_to_int)))

#Abra ocaciones que la conversion no podra ser
w = int("Hola")
print("W con valor {} es del tipo {}".format(z_to_int, type(z_to_int)))