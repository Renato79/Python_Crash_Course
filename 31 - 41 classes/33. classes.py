class Car:
    """A simple attempt to represent a Car"""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

# Instance
my_car = Car('Ford', 'Raptor', 2021)

print(my_car.get_descriptive_name())





# To make the class more interesting, let’s add an attribute that 
# changes over time. We’ll add an attribute that stores the car’s 
# overall mileage.
#
# Setting a Default Value for an Attribute
#
# When an instance is created, attributes can be defined without being
# passed in as parameters. These attributes can be defined in the 
# __init__() method, where they are assigned a default value.
#
# Let’s add an attribute called odometer_reading that always starts 
# with a value of 0. We’ll also add a method read_odometer() that helps
# us read each car’s odometer:
#
# Creating a Bus (autobus) class
class Bus:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0 # Setting a Default Value for an Attribute
    
    def what_mode(self):
        """Return one string full description of the bus"""
        bus_model = f"{self.make} {self.model} {self.year}"
        return bus_model.title()
    
    def bus_odometer(self):
        """Check KM"""
        print(f"This Bus has {self.odometer} km.")

# Instances:
bus = Bus('Fiat', 'Fibus', 2008)

print(bus.what_mode())
bus.bus_odometer()



# Modifying an Attribute’s Value Directly
bus.odometer = 2000 # access the attribute directly
bus.bus_odometer() 

# testing if I can access values from here:
print(bus.make, bus.model, bus.year) # Yep it works, then you need to use self only inside the Class!





print()
# It can be helpful to have methods that update certain attributes for 
# you. Instead of accessing the attribute directly, you pass the new 
# value to a method that handles the updating internally.
#
# Modifying an Attribute’s Value Through a Method
# Let's write the class again for practicing

class Moto:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.km = 0
    def read_km(self):
        print(f"This {self.make.title()} {self.model} has {self.km}km")
        
    def update_km(self, km):
        if km >= self.km:
            self.km = km
        else:
            print(f"{km}??? Your are trying to roll back the odometer!")

moto = Moto('Honda', 'CBR', '2012')

moto.update_km(700)
moto.read_km()
print(f"Current: {moto.km}km")

moto.update_km(400)
moto.read_km()
print(f"Current: {moto.km}km")
