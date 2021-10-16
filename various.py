nums = list(range(1, 11))

for a in reversed(nums):
    print(a)


name = "ReNaTo"

print(name.lower())


toppings = [ 
        'tomato', 'cheese'
        'unouno', 'duedue'
]


numbers = [ 1, 2, 3, 4 ]
again = [ 5, 6, 7, 8 ]

numbers = again[:]

new_list = [ numbers[0], 2 ]
print(f"Value: {new_list}")
print()



my_list = [
    12, 43, 19,
    29, 1, 77,
    56, 31, 34,
    62, 5, 88
]

ok = []



while my_list:
    min = my_list[0]
    for x in my_list:
        if x < min:
            min = x

    ok.append(min)
    my_list.remove(min)

print(ok)

print()
print()

l = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]

for i in range(len(l)):
    for j in range(i + 1, len(l)):

        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]

print(l)


var1 = 200
var2 = var1

var1 = 300

print(f"var1: {var1}")
print(f"var2: {var2}")

print("\n\n\n\n")

name = "Renato is my name."

print(len(name))

for a in name:
    if a == 'a':
        continue # pass gives the same result
    else:
        print(a)
print("\n\n\n")



guests = ['tom', 'jerry', 'spencer', 'ami', 'patty']

print()
print(f"An invitation has been sent for {guests[0].title()}.")
print(f"An invitation has been sent for {guests[1].title()}.")
print(f"An invitation has been sent for {guests[2].title()}.")
print(f"An invitation has been sent for {guests[3].title()}.")
print(f"An invitation has been sent for {guests[4].title()}.")
print()
print(guests[2:4])

print(name[3:6])



pizzas = ('margherita', 'capricciosa', 'pepperoni', 'bianca')

my_list = list(pizzas)
my_list.append('diavola')

new_tuple = tuple(my_list)

print(new_tuple)

print("\n\n\n")


def plus_one(number):
    return number + 1

add_one = plus_one
print(add_one(5))

print(id(add_one))

print(hex(id(add_one)))

print(add_one)