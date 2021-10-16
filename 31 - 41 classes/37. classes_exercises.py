# 9-1. Restaurant: Make a class called Restaurant. The __init__() 
# method for Restaurant should store two attributes: a restaurant_name
# and a cuisine_type. Make a method called describe_restaurant() that 
# prints these two pieces of information, and a method called 
# open_restaurant() that prints a message indicating that the 
# restaurant is open.
#
# 9-4. Number Served: Start with your program from Exercise 9-1 
# Add an attribute called number_served with a default value of 0. 
# Create an instance called restaurant from this class. Print the 
# number of customers the restaurant has served, and then change
# this value and print it again.
#
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new 
# number and print the value again.
#
# Add a method called increment_number_served() that lets you increment 
# the number of customers who’ve been served. Call this method with any
# number you like that could represent how many customers were served 
# in, say, a day of business.

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

restaurant = Restaurant('gold pizza','italian')

print(restaurant.info())

restaurant.count_customers()

restaurant.open()

restaurant.set_number_served(12)

restaurant.count_customers()






print()
# 9-3. Users: Make a class called User. Create two attributes called 
# first_name and last_name, and then create several other attributes
# that are typically stored in a user profile. Make a method called
# describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized 
# greeting to the user.
# Create several instances representing different users, and call both
# methods for each user.
#
# 9-5. Login Attempts: Add an attribute called login_attempts to your 
# User class from Exercise 9-3 (page 162). Write a method called 
# increment_login_attempts() that increments the value of 
# login_attempts by 1. Write another method called reset_login_attempts()
# that resets the value of login_attempts to 0.
#
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was
# incremented properly, and then call reset_login_attempts(). 
# Print login_attempts again to make sure it was reset to 0.

class User:
    def __init__(self, first_name, last_name, email):
        """ Attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.full_name = first_name + " " + last_name
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


user = User('renato', 'bianco', 'renato.bianco@hotmail.com')

user.greeting()
user.info()

user.increment_login_attempts()
print(f"Attempts: {user.login_attempts}")
user.increment_login_attempts()
print(f"Attempts: {user.login_attempts}")
user.increment_login_attempts()
print(f"Attempts: {user.login_attempts}")

user.reset_login_attempts()
print(f"Attempts: {user.login_attempts}")
