import DZ_1_OOP.src.figure as fig

class Rectangle(fig.Figure):

    def __init__(self, side_1, side_2):
        self.name = "Rectangle"
        self.side_1 = side_1
        self.side_2 = side_2

    def find_perimetr(self):
        self.perimetr = 2 * (self.side_1 + self.side_2)
        return self.perimetr

    def find_area(self):
        self.area = self.side_1 * self.side_2
        return self.area
