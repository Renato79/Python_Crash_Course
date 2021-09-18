cars = ['fiat', 'mazda', 'volvo', 'fiesta', 'citroen', 'panda', 'ferrari', 'peugeot']

print()
print(cars) # Print the list
print()
print("Sort the list permanently:")
cars.sort() # Sort the list permanently
print(cars)
print()
print("Sort the list in reverse permanently:")
cars.sort(reverse=True) # Sort the list in reverse permanently
print(cars)
print()


# Sorting a List Temporarily with the sorted() Function
# sorted() is a finction, not a method
print("Sort the list temporarely:")
print(sorted(cars))
print()
print("Sort the list temporarely and reversed:")
print(sorted(cars, reverse=True))
print()


# Reversing the order of the list
# reverse() method doesn't order alphabetically, it simply reverses the order of the list
print("Reversing the list:")
print(cars)
cars.reverse()
print(cars)
print()


# Finding the Length of a List
print(len(cars))
print()