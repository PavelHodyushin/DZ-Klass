class Car:
    price = 1000000

    def __init__(self, my_car):
        self.my_car = my_car
        print('Моя машина')

    def horse_powers(self):
        self.horse_power = 250
        return self.horse_power

class Nissan(Car):
    price = 500000

    def horse_powers(self):
        self.horse_power = 150
        return self.horse_power

class Kia(Car):
    price = 250000

    def horse_powers(self):
        self.horse_power = 100
        return self.horse_power

my_car1 = Car('Хонда')
print(my_car1.my_car)
print(my_car1.price)
print(my_car1.horse_powers())
my_car2 = Nissan('Патрол')
print(my_car2.my_car)
print(my_car2.price)
print(my_car2.horse_powers())
my_car3 = Kia('Рио')
print(my_car3.my_car)
print(my_car3.price)
print(my_car3.horse_powers())