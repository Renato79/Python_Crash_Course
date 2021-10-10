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
        lottery = random.choice(new_tuple)
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
        print("Found.")
        break