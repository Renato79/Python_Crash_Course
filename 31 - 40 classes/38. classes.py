# Inheritance
#
# You don’t always have to start from scratch when writing a class.
# If the class you’re writing is a specialized version of another class
# you wrote, you can use inheritance. When one class inherits from 
# another, it takes on the attributes and methods of the first class. 
# The original class is called the parent class, and the new class is
# the child class. The child class can inherit any or all of the 
# attributes and methods of its parent class, but it’s also free to 
# define new attributes and methods of its own.
#
# The __init__() Method for a Child Class
#
# When you’re writing a new class based on an existing class, you’ll 
# often want to call the __init__() method from the parent class. This
# will initialize any attributes that were defined in the parent 
# __init__() method and make them available in the child class.
print()
print()
print("Inheritance")
# Let’s start by making a simple version of the ElectricCar class,
# which does everything the Car class does:
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    
    def read_model(self):
        full_info = f"{self.make} {self.model} {self.year}. KM: {self.odometer}."
        return full_info.title()
    
    def read_odometer(self):
        print(f"This car has run for {self.odometer} kilometers.")
    
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

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    
my_tesla = ElectricCar('tesla', 'model y', 2019)

print(my_tesla.read_model())

# DESCRIPTION OF THE CLASS ABOVE:
#
# ****** NOTE ******: When you create a child class, the parent class
# must be part of the current file and must appear before the child 
# class in the file.
#
# The name of the parent class must be included in parentheses in the
# definition of a child class.
#
# The __init__() method takes in the information required to make a 
# Car instance.
#
# The super() function is a special function that allows you to call 
# a method from the parent class. This line tells Python to call 
# the __init__() method from Car, which gives an ElectricCar instance 
# all the attributes defined in that method. The name super comes from
# a convention of calling the parent class a superclass and the child 
# class a subclass.
#
# We make an instance of the ElectricCar class and assign it to my_tesla.
# This line calls the __init__() method defined in ElectricCar, which in
# turn tells Python to call the __init__() method defined in the parent 
# class Car.
#
# The ElectricCar instance works just like an instance of Car, so now 
# we can begin defining attributes and methods specific to electric cars.


print()
print()
print("Defining Attributes and Methods for the Child Class")
# Defining Attributes and Methods for the Child Class
#
# Let’s add an attribute that’s specific to electric cars (a battery,
# for example) and a method to report on this attribute. We’ll store
# the battery size and write a method that prints a description of the battery:
class myCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    
    def read_model(self):
        full_info = f"{self.make} {self.model} {self.year}. KM: {self.odometer}."
        return full_info.title()
    
    def read_odometer(self):
        print(f"This car has run for {self.odometer} kilometers.")
    
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

class myElectricCar(myCar):
    def __init__(self,make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75
    
    def which_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

tesla = myElectricCar('tesla', 'model y', 2019)
print(tesla.read_model())

tesla.which_battery()

# NOTE: about the class above:
# We added a new attribute self.battery_size and set its initial value 
# to, say, 75. This attribute will be associated with all instances 
# created from the ElectricCar class but won’t be associated with any 
# instances of Car. 
#
# An attribute or method that could belong to any car, rather than one
# that’s specific to an electric car, should be added to the Car class
# instead of the ElectricCar class. Then anyone who uses the Car class
# will have that functionality available as well, and the ElectricCar 
# class will only contain code for the information and behavior specific
# to electric vehicles.








# Overriding Methods from the Parent Class
#
# You can override any method from the parent class that doesn’t fit 
# what you’re trying to model with the child class. To do this, you 
# define a method in the child class with the same name as the method 
# you want to override in the parent class. Python will disregard the
# parent class method and only pay attention to the method you define
# in the child class.
#
# Say the class Car had a method called fill_gas_tank(). This method is
# meaningless for an all-electric vehicle, so you might want to override 
# this method. Here’s one way to do that:
class ElectricCar(Car):
    """ ...previous code here... """
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
# Now if someone tries to call fill_gas_tank() with an electric car, 
# Python will ignore the method fill_gas_tank() in Car and run this
# code instead. When you use inheritance, you can make your child 
# classes retain what you need and override anything you don’t need 
# from the parent class.




print()
print()
print("Instances as Attributes")
# Instances as Attributes
#
# When modeling something from the real world in code, you may find 
# that you’re adding more and more detail to a class. You’ll find
# that you have a growing list of attributes and methods and that your 
# files are becoming lengthy. In these situations, you might recognize
# that part of one class can be written as a separate class. 
# You can break your large class into smaller classes that work together.
#
# For example, if we continue adding detail to the ElectricCar class, 
# we might notice that we’re adding many attributes and methods specific
# to the car’s battery. When we see this happening, we can stop and move
# those attributes and methods to a separate class called Battery. Then
# we can use a Battery instance as an attribute in the ElectricCar class:
class Moto:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    
    def read_model(self):
        full_info = f"{self.make} {self.model} {self.year}. KM: {self.odometer}."
        return full_info.title()
    
    def read_odometer(self):
        print(f"This car has run for {self.odometer} kilometers.")
    
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


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
    
    def battery_type(self):
        print(f"This motorbike has a {self.battery_size}-kWh battery.")
        
    def battery_range(self):
        if self.battery_size <= 75:
            range = 260
        elif self.battery_size > 75 and self.battery_size <= 100:
            range = 350
        
        print(f"This car can go about {range} miles on full charge.")


class ElectricMoto(Moto):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # Instance as Attribute
        self.battery = Battery()

        
honda = ElectricMoto('honda', 'CBR', 2015)

print(honda.read_model())

honda.battery.battery_type()

honda.battery.battery_range()

# As you begin to model more complicated things like electric cars, 
# you’ll wrestle with interesting questions. Is the range of an 
# electric car a property of the battery or of the car? If we’re only
# describing one car, it’s probably fine to maintain the association of
# the method get_range() with the Battery class. But if we’re describing
# a manufacturer’s entire line of cars, we probably want to move
# get_range() to the ElectricCar class. The get_range() method would 
# still check the battery size before determining the range, but it 
# would report a range specific to the kind of car it’s associated with.
# Alternatively, we could maintain the association of the get_range() 
# method with the battery but pass it a parameter such as car_model. 
# The get_range() method would then report a range based on the battery 
# size and car model.
