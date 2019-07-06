class Shape:
    def what_am_i(self):
        return "I am a shape"

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2
    

class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def calculate_perimeter(self):
        return self.side * 4
    
    


rect1 = Rectangle(2, 3)
squ1 = Square(4)

print(rect1.what_am_i())
print(squ1.what_am_i())

