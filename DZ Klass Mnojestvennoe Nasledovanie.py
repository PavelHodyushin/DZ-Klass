class Vehicle:
    vehicle_type = "none"

class Car:
    price = 100000

    def __init__(self, my_car):
        self.my_car = my_car

    def horse_powers(self):
        self.horse_power = 100
        return self.horse_power

class Nissan(Vehicle,Car):
    price = 500000
    vehicle_tupe = "О-о-оо машина подешевела :)"

    def horse_powers(self):
        self.horse_power = 250
        return self.horse_power

juke = Nissan('ниссан жук')
print(juke.my_car)
print(juke.horse_powers())
print(juke.vehicle_tupe)
print(juke.price)
