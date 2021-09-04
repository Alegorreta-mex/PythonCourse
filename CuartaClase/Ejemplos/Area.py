from Clases.CuartaClase.MyModule import Areas
from Clases.CuartaClase.MyModule.Funciones import imprimir




if __name__ == '__main__':
    rectangulo = Areas.Rectangulo(width=2, heigth=5)
    imprimir("El rectangulo", "Area", rectangulo.get_area())
