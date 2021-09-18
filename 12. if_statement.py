# At the heart of every if statement is an expression that can be 
# evaluated as True or False and is called a conditional test.
# == != < <= => >

cars = ['toyota', 'subaru', 'bmw', 'audi']

for car in cars:
    if car.lower() == 'bmw':
        print(car.upper())
    else:
        print(car.title())


age_renato = 42
age_ainhoa = 45

# and
if age_ainhoa == 42 and age_renato == 42:
    print("same age")
else:
    print("not the same age")

# same if can be written in this way
if (age_ainhoa == 42) and (age_renato == 42):
    print("same age")
else:
    print("not the same age")    


# or
if age_renato == 42 or age_ainhoa == 42:
    print("someone here is 42 years old already")
else:
    print("nobody is 42 years old?")


# Checking Whether a Value Is in a List
requested_toppings = [
    'mushrooms',
    'pepperoni',
    'onions',
    'mozzarella',
    'cheese',
    'potatoes',
    'sausages'
]

if 'mushrooms' in requested_toppings:
    print("Ok, mushrooms added.")
if 'sausages' in requested_toppings:
    print("Ok, sausages added.")
if 'tomatoes' not in requested_toppings:
    print("Tomatoes not requested, will be a white pizza!")



numbers = list(range(1, 11))

for n in numbers:
    if n > 5:
        print(n)

age = 18

if age >= 18:
    print("You can vote.")

print()



# ################################## #
# Which triangle is this?            #
# Equilateral, isosceles, scalene    #
# ################################## #

side_1 = 4
side_2 = 44
side_3 = 44

if side_1 == side_2 and side_2 == side_3:
    print("We have an equilateral triangle.")
elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
    print("We have an isosceles triangle.")
else:
    print("We have a scalene triangle.")


print()


# Let's check if there are values in the list 
toppings = []

if toppings:
    for top in toppings:
        print(f"Adding {top} to your pizza!")
    print("Your pizza is ready.")
else:
    print("No toppings in the list, I'll make a plain pizza for you!\n")






users = [
    'renato',
    'ainhoa',
    'admin',
    'pintxi',
    'tili'
]

for user in users:
    if user.lower() == 'admin':
        print("Hello Admin, would you like to see a status report?\n")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.\n")

users.clear()

if users:
    print("Welcome to the new users!\n")
else:
    print("We need to find some users!\n")


print()
print()



# ################# #
# Ordering an array #
# ################# #

# My exercise
my_list = [
    12, 43, 19,
    29, 1, -9, 77,
    56, 31, 34,
    62, 5, 88
]

print(my_list)
print()

temp = []
values = []


values = [ my_list[0] ]

for num in my_list[1:]:
    temp.clear()
    i = 0
    for val in values:
        if num <= val:
            temp.append(num)
            temp.extend(values[i:])
            values = temp[:]
            break
        if num > val:
            temp.append(val)
            i = i + 1
            if len(values) == i:
                temp.append(num)
    values = temp[:]       

print(values)
 

 
print()
print()



# From the web

new_list = []
my_list = [-15, -26, 15, 1, -34, 4, 5, 6, 6, 6, 23, -64, 23, 76]

while my_list:
    min = my_list[0]  
    for x in my_list: 
        if x < min:
            min = x
    new_list.append(min)
    my_list.remove(min)    

print(new_list)



# Very good example from the web:
l = [64, 25, 12, 22, 11, 1, 2, 44, 3, 122, 23, 34]

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]

print(l)