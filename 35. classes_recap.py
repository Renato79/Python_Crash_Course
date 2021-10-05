class Car:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.contakm = 0
    
    def model_info(self):
        print(f"\nThis car is a {self.make.title()} {self.model.title()}. Manufactured in {self.year}.")
    
    def read_km(self):
        print(f"This {self.make.title()} {self.model.title()} has {self.contakm} km.")
    
    def update_km(self, km):
        if km >= self.contakm:
            self.contakm = km
        else:
            print(f"\nYou can't roll back the odometer!")
    

car = Car('ford', 'raptor', 2018)

car.update_km(300)
car.read_km()

car.update_km(400)
car.read_km()

car.contakm = 500
car.read_km()

car.update_km(200)
car.read_km()

car.model_info()