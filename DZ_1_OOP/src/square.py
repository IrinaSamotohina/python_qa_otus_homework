import DZ_1_OOP.src.figure as fig
import math

class Square(fig.Figure):

    def __init__(self, side):
        self.name = "Square"
        self.side = side

    def find_perimetr(self):
        self.perimetr = self.side * 4
        return self.perimetr

    def find_area(self):
        self.area = self.side ** 2
        return self.area
