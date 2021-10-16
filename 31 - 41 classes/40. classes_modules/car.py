class Car:
    def __init__(self, make, model, year):
        self.make = make.title()
        self.model = model.title()
        self.year = year
    
    def show_car(self):
        print(f"Car on sale: {self.make} {self.model} {self.year}")


