class Square:
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4

    def change_size(self, val):
        self.side += val



square1 = Square(10)
print(square1.side)
print(square1.calculate_perimeter())

square1.change_size(10)
print(square1.side)
print(square1.calculate_perimeter())

