import DZ_1_OOP.src.figure as fig
import math

class Triangle(fig.Figure):

    def __init__(self, side_1, side_2, side_3):
        self.name = "Triangle"
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def find_perimetr(self):
        self.perimetr = self.side_1 + self.side_2 + self.side_3
        return self.perimetr

    def find_area(self):
        self.p = self.perimetr/2
        self.area = math.sqrt(self.p*((self.p-self.side_1)*
                                      (self.p-self.side_2)*
                                      (self.p-self.side_3)))
        return self.area
