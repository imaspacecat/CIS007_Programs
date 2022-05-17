import math

class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.__color = color
        self.__filled = filled

    def __str__(self):
        return "color: " + self.__color + " and filled: " + str(self.__filled)

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled




class Triangle(GeometricObject):
    def __init__(self, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + " side2 = " + str(self.__side2) + " side3 =" + str(self.__side3)

    def getSide1(self):
        return self.__side1

    def setSide1(self, side1):
        self.__side1 = side1

    def getSide2(self):
        return self.__side2

    def setSide2(self, side2):
        self.__side2 = side2

    def getSide3(self):
        return self.__side3

    def setSide3(self, side3):
        self.__side3 = side3

    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        area = math.sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))
        return area

    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3


side1, side2, side3 = eval(input("Enter the value for side 1, side 2, and side 3 with a comma separating them: "))
color = input("Enter a color: ")
fill = eval(input("Enter whether the shape should be filled (1/0): "))

tri = Triangle(side1, side2, side3)
tri.setColor(color)
tri.setFilled(fill)

print("Triangle area:", tri.getArea())
print("Triangle perimeter:", tri.getPerimeter())
print("Triangle color:", tri.getColor())
print("Triangle fill:", tri.isFilled())



