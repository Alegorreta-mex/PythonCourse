import math
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def get_qudrant(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo Cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer Cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto Cuadrante"

    def create_vector(self, p2):
        sum_x = self.x + p2.x


point = Point()
