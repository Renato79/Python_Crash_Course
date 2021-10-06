# Passing an Arbitrary Number of Arguments
# Sometimes you won’t know ahead of time how many arguments a function
# needs to accept.
# Python allows a function to collect an arbitrary number of arguments
# from the calling statement.
# The asterisk in the parameter name *toppings tells Python to make an 
# empty tuple called toppings and pack whatever values it receives into
# this tuple.
def make_pizza(*toppings):
    # print(type(toppings)) - result: <class 'tuple'>
    qt = len(toppings)
    if qt > 1:
        top = 'toppings'
    else:
        top = 'topping'
            
    print(f"\nMaking a pizza with the following {top}:")
        
    for topping in toppings:
        print(f"- {topping}")

make_pizza('mozzarella', 'prosciutto cotto', 'panna')
print()
make_pizza('pomodoro')
print()
# This syntax works no matter how many arguments the function receives.





# Mixing Positional and Arbitrary Arguments
# If you want a function to accept several different kinds of arguments,
# the parameter that accepts an arbitrary number of arguments must be 
# placed last in the function definition. Python matches positional 
# and keyword arguments first and then collects any remaining arguments
# in the final parameter.
#
# For example, if the function needs to take in a size for the pizza, 
# that parameter must come before the parameter *toppings:
def make_pizza(size, *toppings):
    if len(toppings) > 1:
        top = 'toppings'
    else:
        top = 'topping'
        
    print(f"Making a {size}-inch pizza with the following {top}:")
    
    for topping in toppings:
        print(f"- {topping.title()}")

make_pizza(12, 'pomodoro')
print()
make_pizza(16, 'mozzarella', 'prosciutto', 'funghi', 'panna')
print()

#######################################################################
# NOTE: You’ll often see the generic parameter name *args, which      #
# collects arbitrary positional arguments like this.                  #
#######################################################################




# Using Arbitrary Keyword Arguments
# Sometimes you’ll want to accept an arbitrary number of arguments, but
# you won’t know ahead of time what kind of information will be passed
# to the function. In this case, you can write functions that accept as
# many key-value pairs as the calling statement provides.
#
# The double asterisks before the parameter **user_info cause Python to
# create an empty dictionary called user_info and pack whatever name-value
# pairs it receives into this dictionary.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['name'] = first
    user_info['surname'] = last
    
    return user_info


user_profile = build_profile('renato', 'bianco', city='cork', country='ireland', employeer='Apple')

print(user_profile)
print()

#######################################################################
# NOTE: You’ll often see the parameter name **kwargs used to collect  #
# non-specific keyword arguments.                                     #
#######################################################################

# order: positional, keyword, and arbitrary values



