class Rectangle:
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return self.width * 2 + self.height * 2


rect1 = Rectangle(4, 40)
rect2 = Rectangle(3.5, 35.7)
print("Width of rectangles is:", rect1.width, rect2.width)
print("Height of rectangles is:", rect1.height, rect2.height)
print("Area of rectangles is:", rect1.getArea(), rect2.getArea())
print("Perimeter of rectangles is:", rect1.getPerimeter(), rect2.getPerimeter())

