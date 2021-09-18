# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99). 
# Make two new dictionaries representing different people, and store all
# three dictionaries in a list called people. Loop through your list of
# people. As you loop through the list, print everything you know about each person.


person_1 = {
    'name': 'ainhoa',
    'surname': 'bilbao lodosa',
    'city': 'cork',
    'food': 'cheese',
    'likes': 'speaking'    
}

person_2 = {
    'name': 'renato',
    'surname': 'bianco',
    'city': 'cork',
    'food': 'pizza',
    'likes': 'coding'
}

person_3 = {
    'name': 'elliot',
    'surname': 'alderson',
    'city': 'new york',
    'food': 'fries',
    'likes': 'hacking'
}

people = [person_1, person_2, person_3]

print(f"\nWe have {len(people)} people in our list, let's have a look:")

for person in people:
    fullname = f"{person['name'].title()} {person['surname'].title()}" 
    location = person['city'].title()
    food = person['food'].title()
    likes = person['likes'].title()
    
    print(f"\nFull name: {fullname}")
    print(f"Location: {location}")
    print(f"Favourite food: {food}")
    print(f"Hobby: {likes}")





# 6-8. Pets: Make several dictionaries, where each dictionary represents
# a different pet. In each dictionary, include the kind of animal and 
# the owner’s name. Store these dictionaries in a list called pets. 
# Next, loop through your list and as you do, print everything you know
# about each pet.

pet_1 = {
    'kind': 'cat',
    'name': 'tili',
    'age': 10,
    'likes': 'fish'
}

pet_2 = {
    'kind': 'cat',
    'name': 'pintxi',
    'age': 11,
    'likes': 'prawns'
}

pet_3 = {
    'kind': 'dog',
    'name': 'lassie',
    'age': 12,
    'likes': 'bones'
}

pets = [pet_1, pet_2, pet_3]

print(f"\nWe have {len(pets)} puppies in the list:\n")

for puppy in pets:
    kind = puppy['kind']
    name = puppy['name'].title()
    age = puppy['age']
    likes = puppy['likes']
    print(f"{name} is a {kind} {age} years old and loves {likes}.")

print()




# 6-9. Favorite Places: Make a dictionary called favorite_places. 
# Think of three names to use as keys in the dictionary, and store one
# to three favorite places for each person. To make this exercise a bit
# more interesting, ask some friends to name a few of their favorite 
# places. Loop through the dictionary, and print each person’s name and
# their favorite places.

fav_places = {
    'renato': 'amsterdam',
    'ainhoa': 'bilbao',
    'peter': 'manhattan',
    'matt': 'los angeles',
    'steve': 'hollywood'
}

print("\nThis is a favourite places excercise:\n")

for name, city in fav_places.items():
    print(f"{name.title()}'s favourite place is {city.title()}")

print()
print()


# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 
# (page 99) so each person can have more than one favorite number.
# Then print each person’s name along with their favorite numbers.
numbers = {
    'ainhoa': [3, 5, 12,],
    'renato': [8, 3, 40],
    'pintxi': [5, 30, 66, 56, 90],
    'tili': [12, 67, 61, 88, 41, 34]
}


for name, number in numbers.items():
    print(f"{name.title()}'s favourite numbers are:")
    for n in number:
        print(n)
print()



# 6-11. Cities: Make a dictionary called cities. Use the names of three
# cities as keys in your dictionary. Create a dictionary of information 
# about each city and include the country that the city is in, its 
# approximate population, and one fact about that city. The keys for 
# each city’s dictionary should be something like country, population, 
# and fact. Print the name of each city and all of the information you 
# have stored about it.

cities = {
    'amsterdam': {
        'country': 'the netherland',
        'population': 250000,
        'product': 'weed'
    },
    
    'paris': {
        'country': 'france',
        'population': 1000000,
        'product': 'cheese'
    },
    
    'rome': {
        'country': 'italy',
        'population': 500000,
        'product': 'carbonara'
    }
}

for city, details in cities.items():
    city = city.title()
    country = details['country'].title()
    population = details['population']
    product = details['product']
    print(f"{city} is in {country} and has {population} inhabitants. Best product of this city is {product}.")






# 6-12. Extensions: We’re now working with examples that are complex 
# enough that they can be extended in any number of ways. Use one of 
# the example programs from this chapter, and extend it by adding new
# keys and values, changing the context of the program or improving the
# formatting of the output.

mundials = {
    'italy': {
        'matches': 4,
        'opponents': ['brazil', 'france', 'portugal', 'spain'],
        'lost': 0,
        'won': 4
    },
    
    'spain': {
        'matches': 5,
        'opponents': ['italy', 'portugal', 'netherland', 'argentina', 'nigeria'],
        'lost': 2,
        'won': 3
    }
}

print("\nWorld Cup:")

for team, result in mundials.items():
    team = team.title()
    matches = result['matches']
    opponent = result['opponents']
    lost = result['lost']
    won = result['won']
    my_string = ""
    
    print(f"\n{team} had {matches} matches.")
    print("The opponents were:")
    for opp in opponent:
        my_string += opp + " " 
    print(my_string.title())
    print(f"{team} lost {lost} matches and won {won}.")