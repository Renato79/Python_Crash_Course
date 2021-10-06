# A dictionary in a list
# A list in a dictionary
# A dictionary in a dictionary


alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
print()



# let's create a list and add 30 dictionaries to the list
aliens = []

for alien in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
print()

# let's see the first 5 in the list
for alien in aliens[:5]:
    print(alien)

# show how many aliens have been created
print(f"\nTotal number of aliens: {len(aliens)}\n")

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
        
for alien in aliens[:5]:
    print(alien)




# Now let's add a list in a dictionary instead

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'cheese', 'parmesan', 'olives']
}

print(f"\nYou ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"Topping: {topping.title()}")




favorite_languages = {
       'jen': ['python', 'ruby'],
       'sarah': ['c'],
       'edward': ['ruby', 'go'],
       'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(language.title())
print()




# Let's add a dictionaries into a dictionary
users = {
    'renato79': {
        'first_name': 'renato',
        'last_name': 'bianco',
        'location': 'cork'
    },
    
    'ainhoa76': {
        'first_name': 'ainhoa',
        'last_name': 'bilbao lodosa',
        'location': 'cork'
    }
}

print(f"We have {len(users)} users:")

for username, user_info in users.items():
    print(f"\nUsername: {username.title()}")
    print(f"\tFull name: {user_info['first_name'].title()} {user_info['last_name'].title()}")
    print(f"\tLocation: {user_info['location'].title()}")
    
#   for key, value in user_info.items():
#       print(f"{key.title()}: {value.title()}")
        