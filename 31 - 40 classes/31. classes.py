# In object-oriented programming you write classes that represent
# real-world things and situations, and you create objects based 
# on these classes.

# Making an object from a class is called instantiation, 
# and you work with instances of a class.

# You’ll store your classes in modules and import classes 
# written by other programmers into your own program files.

# Understanding object-oriented programming will help you see
# the world as a programmer does. It’ll help you really know your 
# code, not just what’s happening line by line, but also the bigger 
# concepts behind it.


# By convention, capitalized names refer to classes in Python.
class Dog:
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name.title()} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name.title()} rolled over!")

# A function that’s part of a class is a method. Everything you learned 
# about functions applies to methods as well; the only practical
# difference for now is the way we’ll call methods.

# The __init__() method is a special method that Python runs 
# automatically whenever we create a new instance based on the Dog class.

# This method has two leading underscores and two trailing underscores, 
# a convention that helps prevent Python’s default method names from 
# conflicting with your method names.

# The self parameter is required in the method definition, and it must
# come first before the other parameters. It must be included in the
# definition because when Python calls this method later (to create an
# instance of Dog), the method call will automatically pass the self 
# argument. Every method call associated with an instance automatically
# passes self, which is a reference to the instance itself; it gives
# the individual instance access to the attributes and methods in the class.

# When we make an instance of Dog, Python will call the __init__() 
# method from the Dog class. We’ll pass Dog() a name and an age as
# arguments; self is passed automatically, so we don’t need to pass
# it. Whenever we want to make an instance from the Dog class, we’ll
# provide values for only the last two parameters, name and age.

# The two variables defined each have the prefix self. Any 
# variable prefixed with self is available to every method in the 
# class, and we’ll also be able to access these variables through any
# instance created from the class. The line self.name = name takes the
# value associated with the parameter name and assigns it to the 
# variable name, which is then attached to the instance being created.
# The same process happens with self.age = age. Variables that are 
# accessible through instances like this are called attributes.

# The Dog class has two other methods defined: sit() and roll_over().
# Because these methods don’t need additional information to run, we
# just define them to have one parameter, self. The instances we create
# later will have access to these methods. In other words, they’ll be 
# able to sit and roll over. For now, sit() and roll_over() don’t do 
# much. They simply print a message saying the dog is sitting or 
# rolling over. But the concept can be extended to realistic situations:
# if this class were part of an actual computer game, these methods 
# would contain code to make an animated dog sit and roll over. If this
# class was written to control a robot, these methods would direct 
# movements that cause a robotic dog to sit and roll over.


# Making an Instance from a Class.
# We assign the instance to the variable my_dog.
# When Python reads this line, it calls the __init__() method in Dog 
# with the arguments 'Willie' and 6.
# The __init__() method creates an instance representing this 
# particular dog and sets the name and age attributes using the values
# we provided. Python then returns an instance representing this dog.
# We can usually assume that a capitalized name like Dog refers to a 
# class, and a lowercase name like my_dog refers to a single instance
# created from a class.
my_dog = Dog('billy', 2)

print(f"My dog's name is {my_dog.name.title()}.")
print(f"{my_dog.name.title()} is {my_dog.age} years old.")
# To access the attributes of an instance, you use dot notation. 
# We access the value of my_dog’s attribute name by writing:
# my_dog.name


# calling methods
my_dog.sit()
my_dog.roll_over()




# Creating Multiple Instances
# You can create as many instances from a class as you need. 
# Let’s create a second dog called your_dog:
your_dog = Dog('Bodi', 10)

print(f"Your dog's name is {your_dog.name.title()} and is {your_dog.age} years old.")

your_dog.sit()
your_dog.roll_over()

print(f"{my_dog.name.title()} and {your_dog.name.title()} are friends.")




"""
# My own Class

class Ordina:
    
    def __init__(self, numbers):
        self.numbers = numbers
    
    def order(self):
        arr = self.numbers
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if l[i] > l[j]:
                    l[i], l[j] = l[j], l[i]


my_list = [1, 45, 12, 34, 95, 90, 13, 55]

aggiusta = Ordina(my_list)

"""