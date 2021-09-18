# A dictionary in Python is a collection of key-value pairs. Each key 
# is connected to a value, and you can use a key to access the value 
# associated with that key. A key’s value can be a number, a string, a
# list, or even another dictionary. In fact, you can use any object 
# that you can create in Python as a value in a dictionary.

alien_0 = {'color':'green', 'points':5}

print()
print(alien_0['color'])
print(alien_0['points'])

print(alien_0)

new_points = alien_0['points']

print(f"\nYou've just earned new {new_points} points!\n")


# Dictionaries are dynamic structures, and you can add new key-value
# pairs to a dictionary at any time. For example, to add a new key-value
# pair, you would give the name of the dictionary followed by the new 
# key in square brackets along with the new value.
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)


# Creating an empty dictionary
# Typically, you’ll use empty dictionaries when storing user-supplied 
# data in a dictionary or when you write code that generates a large 
# number of key-value pairs automatically.
alien_0 = {}

print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modifying Values in a Dictionary
alien_0['color'] = 'yellow'

print(f"The alien is now {alien_0['color']}")

alien_0['x_position'] = 0
alien_0['y_position'] = 20
alien_0['speed'] = 'medium'
print(alien_0)

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"\nNew position: {alien_0['x_position']}\n")



# Removing Key-Value Pairs
# When you no longer need a piece of information that’s stored in a
# dictionary, you can use the del statement to completely remove a 
# key-value pair. All del needs is the name of the dictionary and the 
# key that you want to remove.
# For example, let’s remove the key 'points' from the alien_0 dictionary 
# along with its value:

# Be aware that the deleted key-value pair is removed permanently.
del alien_0['points']

print(alien_0)


favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

language = favourite_languages['edward'].title()

print(f"\nEdward's favourite language is: {language}\n\n")


# For dictionaries, specifically, you can use the get() method to set a
# default value that will be returned if the requested key doesn’t exist.
# The get() method requires a key as a first argument. As a second 
# optional argument, you can pass the value to be returned if the key 
# doesn’t exist:
point_value = alien_0.get('points', 'No point value assigned\n')
print(point_value)

# another example
dic = {"A":1, "B":2}
# dic['C'] = 3
print(dic.get("A"))
# If you leave out the second argument in the call to get() and the key 
# doesn’t exist, Python will return the value None. The special value 
# None means “no value exists.” This is not an error: it’s a special 
# value meant to indicate the absence of a value.
print(dic.get("C"))
print(dic.get("C","Not Found ! "))























