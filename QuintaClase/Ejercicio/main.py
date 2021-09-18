class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def get_cuadrant(self):
        if self.x > 0 and self.y > 0:
            return "cuadran 1"
        elif self.x < 0 and self.y > 0:
            return "cuadran 2"
        elif self.x < 0 and self.y < 0:
            return "cuadran 3"
        elif self.x > 0 and self.y < 0:
            return "cuadran 4"
        elif self.x == 0 and self.y != 0:
            return "Eje Y"
        elif self.x != 0 and self.y == 0:
            return "Eje X"
        else:
            return "origen"
