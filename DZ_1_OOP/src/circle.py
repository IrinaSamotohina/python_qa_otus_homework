import DZ_1_OOP.src.figure as fig
import math

class Circle(fig.Figure):

    def __init__(self, radius):
        self.name = "Circle"
        self.radius = radius

    def find_perimetr(self):
        self.perimetr = 2 * math.pi * self.radius
        return self.perimetr

    def find_area(self):
        self.area = round(math.pi * self.radius ** 2, 3)
        return self.area
