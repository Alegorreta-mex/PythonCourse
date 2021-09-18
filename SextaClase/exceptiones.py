class MyException(Exception):
    def mimetodo(self):
        print("Algo salio realmente mal")


try:
    x = 1/0
except:
    print("Hola")
try:
    try:
        x = 1 / 2
        list = [1, 2, 3, 4]
        print(list[4])
        print(x)
    # except ZeroDivisionError:
    #     print("No se puede dividir entre 0")
    # except IndexError as e:
    #     print(print(e))
    except:
        print("Error desconocido")
        raise MyException()
except MyException as e:
    e.mimetodo()

print("Termine Codigo")
