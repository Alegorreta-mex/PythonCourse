from .Constants import PI


class Rectangulo():
    def __init__(self, heigth, width):
        self.height = heigth
        self.width = width

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_area(self):
        return self.width * self.height


class Circulo():
    pi = PI

    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        return self.pi * (2 * self.radius)

    def get_area(self):
        return self.pi * (pow(self.radius, 2))


class Triangulo():
    pass

class Rombo():
    pass


class Trapecio():
    pass

class Palalerogramo():
    pass

class NAgono():
    pass


