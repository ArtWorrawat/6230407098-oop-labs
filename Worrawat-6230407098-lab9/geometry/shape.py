from abc import abstractmethod
import random


class Shape:
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        self.radius = radius
        super(Circle, self).__init__(color)

    def set_radius(self, radius):
        self.radius = radius

    @staticmethod
    def get_num_circles(num):
        return num

    def draw(self):
        print("Drawing a circle with radius", self.radius)

class Rectancle(Shape):
    def __init__(self, color, width, height):
        self.width = width
        self.height = height
        super(Rectancle, self).__init__(color)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def print_area(self):
        print(f"Rectangle width {self.width} height {self.height} has area as {self.width * self.height}")

    def draw(self):
        print(f"Drawing a rectangle with width {self.width} height {self.height}")

    def get_num_rectangles(num):
        return num

if __name__ == '__main__':
    circles = []
    rectangles = []
    NUM_OBJECTS = 3
    MIN = 10
    MAX = 20
    colors = ["green", "yellow", "blue", "red", "pink"]
    for i in range(NUM_OBJECTS):
        color = random.choice(colors)
        radius = random.randint(MIN, MAX)
        circles.append(Circle(color, radius))
        circles[i].draw()
    print(f"Num circles is {Circle.get_num_circles(NUM_OBJECTS)}")

    for i in range(NUM_OBJECTS):
        color = random.choice(colors)
        width = random.randint(MIN, MAX)
        height = random.randint(MIN, MAX)
        rectangles.append(Rectancle(color, width, height))
        rectangles[i].draw()
        rectangles[i].print_area
    print(f"Num rectangle is {Rectancle.get_num_rectangles(NUM_OBJECTS)}")