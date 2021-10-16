# 9-1. Restaurant: Make a class called Restaurant. The __init__() 
# method for Restaurant should store two attributes: a restaurant_name
# and a cuisine_type. Make a method called describe_restaurant() that
# prints these two pieces of information, and a method called 
# open_restaurant() that prints a message indicating that the 
# restaurant is open.

# Make an instance called restaurant from your class. Print the two
# attributes individually, and then call both methods.

class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        name = self.restaurant_name
        food = self.cuisine_type

        print(f"We ordered {food} food at {name}'s!")
        
    def open_restaurant(self):
        name = self.restaurant_name
        print(f"{name} is open!")

# Instance
restaurant = Restaurant('Da gino', 'Italian')

restaurant.describe_restaurant()
restaurant.open_restaurant()







# 9-2. Three Restaurants: Start with your class from Exercise 9-1. 
# Create three different instances from the class, and call 
# describe_restaurant() for each instance.
# I will write a new class to practice.

class Pub:
    
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    
    def desc_pub(self):
        print(f"{self.name} is a pub that provides {self.cuisine} cuisine.")

    def open_pub(self):
        print(f"{self.name} is now open!")

# Instance 1
pub_1 = Pub('Mermaid\'s', 'German')
# Instance 2
pub_2 = Pub('Oliver Plunkett', 'Irish')
# Instance 3
pub_3 = Pub('Old Oak', 'British')

pub_1.desc_pub()
pub_1.open_pub()

pub_2.desc_pub()
pub_2.open_pub()

pub_3.desc_pub()
pub_3.open_pub()






# 9-3. Users: Make a class called User. Create two attributes called 
# first_name and last_name, and then create several other attributes
# that are typically stored in a user profile. Make a method called
# describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized 
# greeting to the user.
# Create several instances representing different users, and call both
# methods for each user.

class User:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"My user's full name is: {self.first_name.title()} {self.last_name.title()}.")
    
    def greet_user(self):
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"Hello {full_name}!")


# Instance 1
user_1 = User('renato', 'bianco')

# Instance 2
user_2 = User('ainhoa', 'bilbao lodosa')

# Instance 3
user_3 = User('little', 'john')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()

