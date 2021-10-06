# 6-1. Person: Use a dictionary to store information about a person you
# know. Store their first name, last name, age, and the city in which
# they live. You should have keys such as first_name, last_name, age, 
# and city. Print each piece of information stored in your dictionary.

person = {
    'name': 'ainhoa',
    'surname': 'bilbao lodosa',
    'city': 'cork',
    'food': 'cheese',
    'likes': 'speak'    
}

for details in person:
    print(f"{details.title()}: {person[details].title()}")
    
print(f"\nFirst name: {person['name'].title()}")
print(f"Last name: {person['surname'].title()}")
print(f"City: {person['city'].title()}")
print(f"Favourite food: {person['food'].title()}")
print(f"What she likes: {person['likes'].title()}\n")


# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite 
# numbers. Think of five names, and use them as keys in your dictionary.
# Think of a favorite number for each person, and store each as a value 
# in your dictionary. Print each person’s name and their favorite number.
# For even more fun, poll a few friends and get some actual data for your 
# program.

numbers = {
    'ainhoa': 3,
    'renato': 8,
    'pintxi': 5,
    'tili': 12
}

for number in numbers:
    print(f"{number.title()}: {numbers[number]}")

print()



# 6-3. Glossary: A Python dictionary can be used to model an actual 
# dictionary. However, to avoid confusion, let’s call it a glossary.

# Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store 
# their meanings as values.
# Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the
# word on one line and then print its meaning indented on a second line.
# Use the newline character (\n) to insert a blank line between each 
# word-meaning pair in your output.

glossary = {
    'if': 'condition',
    'for': 'loop',
    'print': 'display on screen',
    'while': 'loop',
    'sort': 'order'
}

for word in glossary:
    print(f"{word.title()}: {glossary[word].title()}")
