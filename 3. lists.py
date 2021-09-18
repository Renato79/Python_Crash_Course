# append() insert() del pop() remove()

# list
names = ['renato','ainhoa','tili','pintxi']

# Python returns its representation of the list, including the square brackets:
print(names)

# To access an element in a list, write the name of the list followed by the index
print(names[0])

# you can format the element 'renato' more neatly by using the title() method
print(names[0].title())

print("")

for a in names:
    print(a)


print("")

# last item
print(names[-1])
# second to last item
print(names[-2])

print("")

message = f"Hello Sir {names[0].title()}"

print(message)

print("")

print(f"My name is {names[0].title()}, my girlfriend's name is {names[1].title()}, and we have two beautiful cats, {names[2].title()} and {names[3].title()}.")

print("")

motorcycles = ['honda', 'yamaha', 'suzuki']

# Changing the value of an item in a list
motorcycles[0] = 'maserati'

print(motorcycles[0].title())

print("")


# Add an element at the end of the list
motorcycles.append('ducati')

print(motorcycles)

print("")

# Let's create an empty list, then we add elements to the list
players = []

players.append('renato')
players.append('ainhoa')
players.append('tili')
players.append('pintxi')

print(players)

# Insert an element in a specific index
players.insert(2,'JOHN')

print(players)

print("")

# Delete an element from the list
del players[2]
print(players)

print("")


# Remove element and use it
popped = players.pop()
print(players)
print(popped.title())

print("")

# Popping Items from any Position in a List
popped2 = players.pop(0)
print(players)
print(popped2.title())

print("")


# Creating a new list
members = ['renato','ainhoa','tili','pintxi','little john', 'tiffany']
print(members)

# If you only know the value of the item you want to remove, you can use the remove() method.
members.remove('little john')
print(members)

print("")

# You can also use the remove() method to work with a value that’s being removed from a list.
# Note: The remove() method deletes only the first occurrence of the value you specify. 
# If there’s a possibility the value appears more than once in the list, 
# you’ll need to use a loop to make sure all occurrences of the value are removed.
too_drunk = 'tiffany'
members.remove(too_drunk)
print(members)

print("")


