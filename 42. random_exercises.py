# TRY IT YOURSELF

# 9-13. Dice: Make a class Die with one attribute called sides, which 
# has a default value of 6. Write a method called roll_die() that prints
# a random number between 1 and the number of sides the die has. Make a
# 6-sided die and roll it 10 times.
#
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.
import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        draw = []
        if self.sides == 6:
            for a in range(0, 11): 
                draw.append(random.randint(1, 6))
        else:
            for a in range(0, 21):
                draw.append(random.randint(1, self.sides))
        print(*draw)


die = Die(6)

die.roll_die()





# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers 
# and five letters. Randomly select four numbers or letters from the 
# list and print a message saying that any ticket matching these four
# numbers or letters wins a prize.

my_tuple = (
    1, 2, 3, 
    4, 5, 6,
    7, 8, 9,
    10, 'a', 'b',
    'c', 'd', 'e',
    )

ticket = []
lim = 1

while lim <= 4:
    lottery = random.choice(my_tuple)
    if lottery not in ticket:
        ticket.append(lottery)
        lim += 1

print("Any ticket matching these four numbers or letters wins a prize: ", *ticket)





# 9-15. Lottery Analysis: You can use a loop to see how hard it might 
# be to win the kind of lottery you just modeled. Make a list or tuple
# called my_ticket. Write a loop that keeps pulling numbers until your
# ticket wins. Print a message reporting how many times the loop had to
# run to give you a winning ticket.
import os

os.system('clear')

new_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
ticket = []
my_ticket = str(7564)
new_ticket = ""

counter = 0

print(f"Combination: {my_ticket}\n\r")


while my_ticket != new_ticket:
    lim = 1
    new_ticket = ""
    ticket = []
    """Generating the winning ticket"""
    while lim <= 4:
        lottery = random.choice(new_tuple)
        if lottery not in ticket:
            ticket.append(lottery)
            lim += 1
        
    for digits in ticket:
        new_ticket += str(digits)

    counter += 1
    
    print(new_ticket, end = "\r")

print(f"\n\nGenerated {counter} combinations before guessing the winning ticket!")


"""
import os

os.system('clear')

new_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
ticket = []
my_ticket = str(7564)
new_ticket = ""

counter = 0

print(f"Combination: {my_ticket}")
print("Generating combinations:")

while my_ticket != new_ticket:
    lim = 1
    new_ticket = ""
    ticket = []

    while lim <= 4:
        lottery = random.choice(new_tuple)
        if lottery not in ticket:
            ticket.append(lottery)
            lim += 1
        
    for digits in ticket:
        new_ticket += str(digits)

    counter += 1
    
    print(new_ticket, end = "\r")

print(f"\nGenerated {counter} combinations before guessing the winning ticket!")
"""
# 9-16. Python Module of the Week: One excellent resource for exploring 
# the Python standard library is a site called Python Module of the Week.
# Go to https://pymotw.com/ and look at the table of contents. Find a 
# module that looks interesting to you and read about it, perhaps 
# starting with the random module.
