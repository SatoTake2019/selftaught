class Horse:
    def __init__(self, name):
        self.name = name
        
class Person:
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse


kita_horse = Horse("キタサン")
take_rider = Person("武豊", kita_horse)

print(take_rider.horse.name)
