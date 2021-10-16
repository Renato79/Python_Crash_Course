# 10-11. Favorite Number: Write a program that prompts for the user’s 
# favorite number. Use json.dump() to store this number in a file. 
# Write a separate program that reads in this value and prints the 
# message, “I know your favorite number! It’s _____.”
import json

filename = 'test_files/fav_number.txt'

def get_number():
    """Read the favourite number from the file"""
    try:
        with open(filename) as f:
            number = json.load(f)
        return number
    except FileNotFoundError:
        return None


def ask_number():
    """Prompting fav number and save in json file"""
    number = input("What is your favourite number? ")

    with open(filename, 'w') as f:
        json.dump(number, f)

    print("Thank you! Next time I will remember that your " 
          f"favourite number is {number}!")


num = get_number()

if num:
    print(f"Your favourite number is {num}.")
    print("I'll see you soon!")
else:
    ask_number()





# 10-12. Favorite Number Remembered: Combine the two programs from 
# Exercise 10-11 into one file. If the number is already stored, report
# the favorite number to the user. If not, prompt for the user’s 
# favorite number and store it in a file. Run the program twice to see 
# that it works.

# Already completed in one file. Passing to the next




# 10-13. Verify User: The final listing for remember_me.py assumes 
# either that the user has already entered their username or that the
# program is running for the first time. We should modify it in case
# the current user is not the person who last used the program.
#
# Before printing a welcome back message in greet_user(), ask the user
# if this is the correct username. If it’s not, call get_new_username()
# to get the correct username.

filepath = 'test_files/user.json'

def get_user():
    """Check the name saved in the json file and returns it if found"""
    try:
        with open(filepath) as f:
            name = json.load(f)
        return name
    except FileNotFoundError:
        return None

def create_user(name):
    """Save the username passed as parameter in the json file"""
    with open(filepath, 'w') as f:
        json.dump(name, f)
    print(f"Username saved. We'll remeber you when you come back {name}!")

def greet_user():
    """Greet the user if an existing user, otherwise will create a new one"""
    name = input("Please enter your username: ")
    saved_name = get_user()
    if saved_name == name:
        print(f"Welcome back {name}!")
    else:
        create_user(name)

greet_user()