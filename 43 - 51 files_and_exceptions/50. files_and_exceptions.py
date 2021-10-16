# Storing Data (JSON)

# The json module allows you to dump simple Python data structures into
# a file and load the data from that file the next time the program runs.

# The json.dump() function takes two arguments: a piece of data to store
# and a file object it can use to store the data.

# Here’s how you can use json.dump() to store a list of numbers:
import json


numbers = [3, 6, 12, 34, 1, 7]

filename = 'test_files/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f) # Storing the list in the json file


with open(filename) as f:
    my_list = json.load(f) # getting the list from the json file

print(my_list) # [3, 6, 12, 34, 1, 7]






# Saving and Reading User-Generated Data
filename = 'test_files/username.json'

username = input("What is your name? ")

with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back {username.title()}!")





#  Load the username, if it has been stored previously.
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back {username.title()}!")







# Refactoring
#
# Often, you’ll come to a point where your code will work, but you’ll
# recognize that you could improve the code by breaking it up into a
# series of functions that have specific jobs. This process is called
# refactoring. Refactoring makes your code cleaner, easier to 
# understand, and easier to extend.
def get_stored_user():
    """Get stored username if available"""
    filename = 'test_files/username2.json'
    try:
        with open(filename) as f:
            user = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return user


def get_new_user():
    """Prompt for new username"""
    user = input("Please choose username: ")
    filename = 'test_files/username2.json'
    
    with open(filename, 'w') as f:
        json.dump(user, f)
    return user

    
def greet_user():
    """Greet the user"""
    username = get_stored_user()
    
    if username:
        print(f"Welcome back {username}!")
    else:
        username = get_new_user()
        print(f"We'll remeber you when you come back {username}!")
# This compartmentalization of work is an essential part of writing 
# clear code that will be easy to maintain and extend.

greet_user()