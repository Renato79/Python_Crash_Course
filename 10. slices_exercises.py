foods = ["bread", "pizza", "eggs", "pasta", "nachos", "mozzarella", "ham", "bacon"]

print(f"The first three items in the list are: {foods[:3]}")
print(f"Three itmes from the middle of the list are: {foods[3:6]}")
print(f"The last three items in the list are: {foods[-3:]}")

friends_foods = foods[:]

foods.append('coke')
friends_foods.append('rum')

print(f"\nThis is my list: {foods}")
print(f"This is my friend's list: {friends_foods}")

print("\nlet's loop!\n")

for food in foods:
    print(food)

print()

for fr_food in friends_foods:
    print(fr_food)

print()

for fd in foods[3:5]:
    print(fd)