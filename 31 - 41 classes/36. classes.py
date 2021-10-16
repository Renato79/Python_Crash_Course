class Car:    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    
    def read_model(self):
        full_details = f"{self.make} {self.model} {self.year}. Km: {self.odometer}."
        return full_details.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer} km.")
    
    def update_odometer(self, km):
        if km >= self.odometer:
            self.odometer = km
        else:
            print(f"You can't roll back the odometer!")
    
    def increase_odometer(self, new_km):
        if new_km >= 1:
            self.odometer += new_km
            print(f"Odometer value increased of {new_km} km.")
        else:
            print(f"You can't roll back the odometer!")
    

car = Car('seat', 'ibiza', 2018)

print(car.read_model())

car.update_odometer(300)
print(car.read_model())

car.update_odometer(200)
print(car.read_model())

car.increase_odometer(50)
print(car.read_model())

car.increase_odometer(-150)
print(car.read_model())