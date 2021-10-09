from car import Car # from car.py import the class Car
from electric_car import ElectricCar as EC # Using an alias

car = Car('ford', 'raptor', 2019)
car.show_car()

print()

tesla = EC('tesla', 'model x', 2015)
tesla.show_car()
tesla.battery.battery_info()
tesla.battery.battery_range()
