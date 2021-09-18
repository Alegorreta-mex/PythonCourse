# from .Constants import PI
from math import sqrt


def get_perimeter(width, height):
    return (2 * width) + (2 * height)


class Rectangulo():
    def __init__(self, heigth, width):
        self.height = heigth
        self.width = width

    @staticmethod
    def get_perimeter(width, height):
        return (2 * width) + (2 * height)

    def get_area(self):
        return self.width * self.height


class Circulo():
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        return self.pi * (2 * self.radius)

    def get_area(self):
        return self.pi * (pow(self.radius, 2))


class Triangulo():
    pass


class Rombo():
    def __init__(self, heigth, width):
        self.height = heigth
        self.width = width

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_area(self):
        cateto1 = self.width / 2
        cateto2 = self.height / 2
        cateto1_pow = pow(cateto1, 2)
        cateto2_pow = pow(cateto2, 2)
        a = sqrt(cateto1_pow + cateto2_pow)
        return a * 4



class Trapecio():
    pass


class Palalerogramo():
    pass


class NAgono():
    pass


print(get_perimeter(5, 6))
