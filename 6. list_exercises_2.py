# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.

places = ['paris', 'amsterdam', 'new york', 'rome', 'bratislava']

# Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.

print()
print(places)
print()

# Use sorted() to print your list in alphabetical order without modifying the actual list.

print(sorted(places))
print()

# Show that your list is still in its original order by printing it.
print(places)
print()

# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print(sorted(places, reverse=True))
print()

# Show that your list is still in its original order by printing it again.
print(places)
print()

# Use reverse() to change the order of your list. Print the list to show that its order has changed.
places.reverse()
print(places)
print()

# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
places.reverse()
print(places)
print()

# Use sort() to change your list so it’s stored in alphabetical order. 
# Print the list to show that its order has been changed.
places.sort()
print(places)
print()

# Use sort() to change your list so it’s stored in reverse alphabetical order. 
# Print the list to show that its order has changed.
places.sort(reverse=True)
print(places)
print()



# Every Function: Think of something you could store in a list. For example, you could make a list of mountains, 
# rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing 
# these items and then uses each function introduced in this chapter at least once.
icecreams = ['panna', 'cioccolato', 'fragola', 'vaniglia', 'nocciola', 'limone', 'banana']

# methods: append(), clear(), copy(), count(), extend(), index(), insert(), pop(), remove(), reverse(), sort()
# functions: len(), sorted()
print()
print("original list:")
print(icecreams)
print()
print("append():")
icecreams.append('stracciatella')
print(icecreams)
print()

print("copy():")
x = icecreams.copy()
print(x)
print()

print("count('banana'):")
trova = icecreams.count('banana')
print(trova)
print()

new_tastes = ['arancio', 'gianduia', 'pistacchio']
print("extend():")
icecreams.extend(new_tastes)
print(icecreams)
print()

print("index():")
dove = icecreams.index('vaniglia')
print(dove)
print()

print("insert():")
icecreams.insert(3, 'melograno')
print(icecreams)
print()

print("pop():")
icecreams.pop()
print(icecreams)
print()

print("remove():")
icecreams.remove('vaniglia')
print(icecreams)
print()

print("reverse():")
icecreams.reverse()
print(icecreams)
print()

print("sort():")
icecreams.sort()
print(icecreams)
print()

print("sort(reverse=True):")
icecreams.sort(reverse=True)
print(icecreams)
print()

print("sorted(icecreams):")
print(sorted(icecreams))
print()

print("sorted(icecreams, reverse=True):")
print(sorted(icecreams, reverse=True))
print()

print("len(icecreams):")
print(len(icecreams))
print()

print("clear():")
icecreams.clear()
print(icecreams)
print()


