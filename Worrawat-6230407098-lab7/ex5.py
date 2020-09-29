import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pow(self.radius, 2) * math.pi

    def get_perimeter(self):
        return 2 * math.pi * self.radius


print("The circle with radius 3 has the area as {:.2f} and the perimeter as {:.2f}".format(Circle(3).get_area(),
                                                                                         Circle(3).get_perimeter()))
print("The circle with radius 4 has the area as {:.2f} and the perimeter as {:.2f}".format(Circle(4).get_area(),
                                                                                         Circle(4).get_perimeter()))
