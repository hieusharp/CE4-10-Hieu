import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distant(self, point):
        dx = (self.x - point.x)
        dy = (self.y - point.y)
        distant = math.sqrt(dx * dx + dy*dy)
        return distant

    def halfway(self, point2):
        central_point = Point((self.x + point2.x) / 2, (self.y + point2.y) / 2)
        central_point.print()
        return central_point

    def reflect_x(self):
        reflect_x = Point(-self.x, self.y)
        reflect_x.print()
        return reflect_x

    def reflect_y(self):
        reflect_y = Point(self.x, -self.y)
        reflect_y.print()
        return reflect_y

    def reflect_O(self):
        reflect_O = Point(-self.x, -self.y)
        reflect_O.print()
        return reflect_O

class Rectangle:
    def __init__(self, position, width, height):
        self.position = position
        self.width = width
        self.height = height

    def area(self):
        area = self.width * self.height
        return area

    def perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def flip(self):
        (self.width, self.height) = (self.height, self.width)
        print("\tAfter Flip: width = {0}, height = {1}".format(self.width, self.height))

    def contain(self, point):
        return self.position.x < point.x < self.position.x + self.width \
            and self.position.y > point.y > self.position.y - self.height