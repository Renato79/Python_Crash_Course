# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of 
# restaurant. Write a class called IceCreamStand that inherits from the
# Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4
# (page 167). Either version of the class will work; just pick the one 
# you like better. Add an attribute called flavors that stores a list
# of ice cream flavors. Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.
class Restaurant:    
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
    
    def info(self):
        info = f"Ristorante {self.name}, {self.cuisine} cuisine."
        return info.title()
    
    def open(self):
        print(f"{self.name.title()} is open!")
    
    def count_customers(self):
        print(f"{self.name.title()} has had {self.number_served} so far!")

    def set_number_served(self, customers):
        self.number_served += customers


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ['lemon', 'chocolate', 'strawberry', 'melon']
        
    def flavor_list(self):
        for taste in self.flavors:
            print(taste.title())


ice_cream = IceCreamStand('Big Shot', 'Italian')

ice_cream.flavor_list()







# 9-7. Admin: An administrator is a special kind of user. Write a class
# called Admin that inherits from the User class you wrote in Exercise 
# 9-3 (page 162) or Exercise 9-5 (page 167). Add an attribute, privileges,
# that stores a list of strings like "can add post", "can delete post", 
# "can ban user", and so on. Write a method called show_privileges() that
# lists the administrator’s set of privileges. Create an instance of 
# Admin, and call your method.
class User:
    def __init__(self, first_name, last_name, email):
        """ Attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.full_name = f"{first_name.title()} {last_name.title()}"
        self.login_attempts = 0

    def info(self):
        print(f"User: {self.full_name.title()}")
        print(f"Email: {self.email}")
    
    def greeting(self):
        print(f"Welcome {self.full_name.title()}")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can ban users", "can change passwords", "can delete posts"]
        
    def show_privileges(self):
        for task in self.privileges:
            print(task)
    
class Admin(User):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.rights = Privileges()


admin = Admin('renato', 'bianco', 'renato.bianco@hotmail.com')

print("\n\nInfo:")
admin.info()

print("\nGreeting:")
admin.greeting()

print("\nPrivileges:")
admin.rights.show_privileges()

# 9-8. Privileges: Write a separate Privileges class. The class should
# have one attribute, privileges, that stores a list of strings as
# described in Exercise 9-7. Move the show_privileges() method to this
# class. Make a Privileges instance as an attribute in the Admin class.
# Create a new instance of Admin and use your method to show its privileges.
# NOTE: (DONE ABOVE)







# 9-9. Battery Upgrade: Use the final version of electric_car.py from 
# this section. Add a method to the Battery class called 
# upgrade_battery(). This method should check the battery size and set
# the capacity to 100 if it isn’t already. Make an electric car with a
# default battery size, call get_range() once, and then call get_range()
# a second time after upgrading the battery. You should see an increase 
# in the car’s range.
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
        
    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100


class ElectricMoto(Moto):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # Instance as Attribute
        self.battery = Battery()


honda = ElectricMoto('honda', 'CBR', 2016)
print()
print()
print(f"battery size: {honda.battery.battery_size}")
honda.battery.battery_range()
honda.battery.upgrade_battery() # Upgrading battery
print(f"battery size: {honda.battery.battery_size}")
honda.battery.battery_range()

print()
print()




# My personal exercise to make sure I got the meaning
class Printer:
    def __init__(self, colour, type):
        self.colour = colour
        self.type = type
        self.sheets = 10

    def check_paper(self):
        print(f"We have {self.sheets} sheets in the printer")
        
        
class Queue:
    def __init__(self, left=10):
        self.left = left
        
    def check_queue(self):
        print(f"There still are {self.left} prints left in the queue")


class Photo(Printer):
    def __init__(self, colour, type):
        super().__init__(colour, type)
        self.queue = Queue()
    
    def print_photo(self):
        if self.sheets != 0:
            print(f"Printing {self.colour} pictures on {self.type} type!")
        else:
            print("You don't have paper lefts!")

photo = Photo('B&W', 'paper')

photo.check_paper()

photo.queue.check_queue()

photo.print_photo()

