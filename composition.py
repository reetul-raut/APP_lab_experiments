class Engine:
    def __init__(self, power):
        self.power = power

class Car:
    def __init__(self):
        self.engine = Engine("150 HP")

car = Car()
print(car.engine.power)
