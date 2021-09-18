# TRY IT YOURSELF - Book Exercises

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
for num in range(1, 21):
    print(num)


# 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
# (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
# I change the exercise above with 100 instead of 1000000
numbers = list(range(1, 101))

print(numbers)



# 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list 
# actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
millions = list(range(1, 1_000_001))

print(min(millions))
print(max(millions))
print(sum(millions))



# 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
# Use a for loop to print each number.
for n in range(1, 20, 2):
    print(n)



# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
for multiple in range(3, 31, 3):
    print(multiple)



# 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. 
# Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), 
# and use a for loop to print out the value of each cube.
cubes = []

for c in range(1, 11):
    cubes.append(c**3)

print(cubes)



# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
compr_cubes = [count**3 for count in range(1, 11)]

print(compr_cubes)