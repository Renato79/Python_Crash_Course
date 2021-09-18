# 7-8. Deli: Make a list called sandwich_orders and fill it with the
# names of various sandwiches. Then make an empty list called 
# finished_sandwiches. Loop through the list of sandwich orders and 
# print a message for each order, such as I made your tuna sandwich. As
# each sandwich is made, move it to the list of finished sandwiches. 
# After all the sandwiches have been made, print a message listing each
# sandwich that was made.

sandwich_orders = ['german', 'bulldog', 'bavarese', 'light']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"\nI've just made your {sandwich.title()} Sandwich for you!")
    
    finished_sandwiches.append(sandwich)

print("\nHere is a list of which sandwiches I have server today:")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()}")




# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8,
# make sure the sandwich 'pastrami' appears in the list at least three
# times. Add code near the beginning of your program to print a message
# saying the deli has run out of pastrami, and then use a while loop to
# remove all occurrences of 'pastrami' from sandwich_orders. Make sure
# no pastrami sandwiches end up in finished_sandwiches.

# I will create a loop to remove all 'pastrami' from the list

sandwich_orders = ['german', 'pastrami', 'bulldog', 'bavarese', 'pastrami', 'pastrami', 'light']

print(sandwich_orders)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)





# 7-10. Dream Vacation: Write a program that polls users about their 
# dream vacation. Write a prompt similar to If you could visit one 
# place in the world, where would you go? Include a block of code that
# prints the results of the poll.

# I will use a dictionary

responses = {}

active = True

while active:
    name = input("What is your name? ")
    city = input("Where would you like to go for a vacation? ")

    responses[name] = city

    repeat = input("Would you like to let someone else to take the poll? ")
    
    if repeat == 'no':
        active = False

print("\n\t--- Poll Results ---")

for name, city in responses.items():
    print(f"\t{name.title()} would like to go to {city.title()}")
    
    