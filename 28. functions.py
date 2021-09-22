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
make_pizza('pomodoro')
# This syntax works no matter how many arguments the function receives.

