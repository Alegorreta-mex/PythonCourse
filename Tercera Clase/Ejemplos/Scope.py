variable_global = "Esta es una variable global"


def test_fun1():
    variable_local = "esta es una variable local"
    print("Podemos acceder a la variable local en la funcion {}".format(variable_local))

class TestClass():
    variable_clase = "Esta es una variable local de la clase"

    def test_func2(self):
        print("{} conseguimos la variable de la clase, por medio del objeto self".format(self.variable_clase))
        try:
            print(variable_clase)
        except:
            print("Pero si lo intentamos sin la variable self no podemos llegar a ese scope")

        print("sin embargo si podemos imprimir la variable global {}".format(variable_global))


test_fun1()
try:
    print(variable_local)
except:
    print("pero no podemos acceder desde fuera de la funcion")

testclass = TestClass()
testclass.test_func2()
