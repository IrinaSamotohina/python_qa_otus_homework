class Figure:

    def __init__(self, name):
        self.name = name
        self.perimetr = 0
        self.area = 0

    def find_perimetr(self):
        return self.perimetr

    def add_perimetr(self, add_perimetr):
        add = self.perimetr + add_perimetr
        return add

    def find_area(self):
        return self.area
