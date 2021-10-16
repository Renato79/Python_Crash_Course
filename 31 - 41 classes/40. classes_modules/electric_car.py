from car import Car

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
    
    def battery_info(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def battery_range(self):
        if self.battery_size == 75:
            range = 200
        else:
            range = 350
        
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()