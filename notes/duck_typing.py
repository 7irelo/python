class Car:
    name = "car"
    def look(self):
        print("The car looks beautiful")
class Bike:
    name = "bike"
    def look(self):
        print("The bike looks beautiful")

class Eric:
    def pick(self, car):
        car.look()
        print(f"You pick the {car.name}")

car = Car()
bike = Bike()
eric = Eric()
eric.pick(bike)