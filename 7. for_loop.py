magicians = ['Alice', 'Carolina', 'David']

for magician in magicians:
    print(f"{magician}, than was a great trick!")
    print(f"I can't wait to see your next trick, {magician}!\n")

print("Thank you, everypne. That was a great magic show!\n")

# Python to start counting at the first value you give it, and it stops when it reaches the second value you provide.
# Result: 1 2 3 4 
for value in range(1, 5):
    print(value)


for val in range(5):
    print("Ciao") # Prints 5 times Ciao

print()



# We can use list() to convert that same set of numbers into a list:
numbers = list(range(1, 6))

print(numbers) # Result: [1, 2, 3, 4, 5]

for i in numbers:
    print(i) # Result 1 2 3 4 5 on new lines

for mynum in range(2, 11, 2):
    print(mynum) # Result 2 4 6 8 10 on new lines


squares = []

for num in range(2, 11):
    sqr = num ** 2
    squares.append(sqr)

print(f"\n{squares}")

# Better way to write more constistent code:
my_squares = []

for n in range(2, 11):
    my_squares.append(n ** 2)
    
print(f"{my_squares}")
print()



# Simple Statistics with a List of Numbers
# 1 10 55
digits = list(range(1, 11))
print(min(digits))
print(max(digits))
print(sum(digits))




# PYTHON - list comprehension (Finally)
new_square = [new_val**2 for new_val in range(1, 20, 2)]

print(new_square)



# Reversed function()
my_arr = list(range(1, 11))

for count in reversed(my_arr):
    print(count)







print()