"""
This code will generate a 5 number combination.

Then it will generate 5 random numbers a time
until it guesses the combination generated.

Once guessed, it will start counting from 0 to 100000,
so that we can compare how which of the two methods
took more time.
"""

import os
import random
import curses

stdscr = curses.initscr()
curses.curs_set(0)  # invisible
os.system('clear')

new_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
ticket = []
my_code = str(75464)
new_code = ""

counter = 0

print(f"Combination: {my_code}\n\r")


while my_code != new_code:
    lim = 1
    new_code = ""
    ticket = []
    """Generating the winning ticket"""
    while lim <= 5:
        lottery = random.choice(new_tuple) # chooses one item
        ticket.append(lottery)
        lim += 1
        
    for digits in ticket:
        new_code += str(digits)

    counter += 1
    
    print(new_code, end = "\r")

print(f"\n\nGenerated {counter} combinations before guessing the winning ticket!\n")

print("\n\rChecking all numbers between 0 and 99999:")

for count in range(0, 100000):
    if str(count) != my_code:
        print("\r", count, end = "\r")
    else:
        print(count, end = "\r")
        print("Found.\r")
        break

print("\n")