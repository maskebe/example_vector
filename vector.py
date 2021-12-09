import math

class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norme(self):
        return math.sqrt(self.x**2 + self.y**2)