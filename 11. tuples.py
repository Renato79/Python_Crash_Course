# When compared with lists, tuples are simple data structures. Use them
# when you want to store a set of values that should not be changed 
# throughout the life of a program.
# Tuples are immutable.

pizzas = ('margherita', 'capricciosa', 'pepperoni', 'bianca')

print(pizzas)

print(pizzas[1:3])

# Tuples are technically defined by the presence of a comma; the 
# parentheses make them look neater and more readable. 
# If you want to define a tuple with one element, you need to include
# a trailing comma:
numbers = (5,)

print(numbers)


# pizzas[0] = 'bianca' would generate an error since the values are 
# immutable

# we associate a new tuple with the variable pizzas. 
# Python doesn’t raise any errors this time, because reassigning 
# a variable is valid:
pizzas = ('melenzane', 'salsiccia', 'diavola')

print(pizzas)

for pizza in pizzas:
    print(pizza.title())

