import DZ_1_OOP.src.triangle as tria
import DZ_1_OOP.src.square as squa
import DZ_1_OOP.src.circle as circ
import DZ_1_OOP.src.figure as Figure


a = tria.Triangle(10, 10, 10)
b = squa.Square(10)
c = circ.Circle(4)

print(Figure.find_perimetr(10, 10, 10))
#print(a.add_perimetr(b.find_perimetr()))
# b.find_perimetr()
# print(b.add_perimetr(a.find_perimetr()))
# c.find_perimetr()
# print(c.add_perimetr(b.find_perimetr()))
