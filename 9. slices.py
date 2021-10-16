players = ["renato", "ainhoa", "tili", "pintxi", "tom", "jerry", "speedy", "willy"]

# Printing a slice
print(players[2:4])

# If you omit the first index in a slice, Python automatically starts 
# your slice at the beginning of the list:
print(players[:3])

# If you want all items from the third item through the last item, you
# can omit the second index:
print(players[3:])

# if we want to output the last three players
print(players[-3:])

# if we want to output all the players except the last three
print(players[:-3])

# You can include a third value in the brackets indicating a slice. If
# a third value is included, this tells Python how many items to skip 
# between items in the specified range.
print(players[1:8:2])


# Loops with slices
for player in players[2:5]:
    print(player.title())
    



# Correct way of copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # or friend_foods = my_foods.copy()

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# In the example above, if we use the following declaration:
# friend_foods = my_foods
# Instead of storing a copy of my_foods in friend_foods, we set friend_foods equal to my_foods. 
# This syntax actually tells Python to associate the new variable friend_foods with the list 
# that is already associated with my_foods, so now both variables point to the same list. 
# As a result, when we add 'cannoli' to my_foods, it will also appear in friend_foods. 
# Likewise 'ice cream' will appear in both lists, even though it appears to be added only to friend_foods.

