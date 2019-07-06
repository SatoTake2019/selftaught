class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return (self.width + self.length) * 2

class Square:
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4

rect1 = Rectangle(2, 3)
print(rect1.calculate_perimeter())

square1 = Square( 3 )
print( square1.calculate_perimeter() )
