# Greeter
# The text at 7 is a comment called a docstring, which describes what
# the function does. Docstrings are enclosed in triple quotes, which
# Python looks for when it generates documentation for the functions in
# your programs.
def greet_user(): # function definition
    """Display a simple greeting."""
    print("Hello!\n")

greet_user() # function call


# Passing information to the function
# The variable username in the definition of greet_user_2() is an example
# of a parameter, a piece of information the function needs to do its job. 
# The value 'renato' in greet_user_2('renato') is an example of an argument.
def greet_user_2(username): # function definition
    print(f"Hello {username.title()}!\n")

greet_user_2("renato") # function call with an argument

#######################################################################
# NOTE:
# People sometimes speak of arguments and parameters interchangeably. 
# Don’t be surprised if you see the variables in a function definition
# referred to as arguments or the variables in a function call referred
# to as parameters.
#######################################################################



# Positional Arguments:
# When you call a function, Python must match each argument in the 
# function call with a parameter in the function definition. The 
# simplest way to do this is based on the order of the arguments 
# provided. Values matched up this way are called positional arguments.
def desc_pet(pet_kind, name): # function definition
    """Display information about a pet."""
    print(f"I have a {pet_kind}.")
    print(f"My {pet_kind}'s name is {name.title()}")

desc_pet('cat', 'tili') # function call
# You can call a function as many times as needed.
desc_pet('dog', 'fido') # function call


# Keyword Arguments:
# A keyword argument is a name-value pair that you pass to a function. 
# You directly associate the name and the value within the argument, 
# so when you pass the argument to the function, there’s no confusion.
#
# In this case the order of keyword arguments doesn’t matter because 
# Python knows where each value should go.
#
# When you use keyword arguments, be sure to use the exact names of the 
# parameters in the function’s definition:
desc_pet(pet_kind='monkey', name='cita') # function call




# Default Values:
# If an argument for a parameter is provided in the function call, 
# Python uses the argument value.
# If not, it uses the parameter’s default value.

def desc_pet_2(pet_name, pet_kind='dog'): # function definition
    print(f"\nI have a {pet_kind}.")
    print(f"My {pet_kind}'s name is {pet_name.title()}\n")
    
desc_pet_2('fido') # function call
# OR
desc_pet_2(pet_name='Lessie') # function call
# Including the argument:
desc_pet_2('birba', 'cat') # function call
# OR
desc_pet_2(pet_name='luna', pet_kind='turtle') # function call
# NOTE: When you use default values, any parameter with a default value 
# needs to be listed after all the parameters that don’t have default 
# values. This allows Python to continue interpreting positional arguments
# correctly.



