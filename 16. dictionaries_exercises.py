# 6-4. Glossary 2: Now that you know how to loop through a dictionary,
# clean up the code from Exercise 6-3 (page 99) by replacing your
# series of print() calls with a loop that runs through the dictionary’s 
# keys and values. When you’re sure that your loop works, add five more 
# Python terms to your glossary. When you run your program again, these 
# new words and meanings should automatically be included in the output.

diet = {
    'breakfast': 'milk and weetabix',
    'first_snack': 'yogurt',
    'lunch': 'chicken',
    'second_snack': 'banana',
    'dinner': 'fish and vegetables'
}

# print only the key values. It would have been the same "for key in diet:", without keys()
print("Print only the key values:")
for key in diet.keys():
    print(key.title())

# print only the values, without the keys
print("\nPrint only the values, without the keys:")
for value in diet.values():
    print(value.title())

# print both the keys and the values
print("\nPrint both the keys and the values:")
for key, value in diet.items():
    print(f"{key.title()}: {value.title()}")




# 6-5. Rivers: Make a dictionary containing three major rivers and the 
# country each river runs through. One key-value pair might be 'nile': 'egypt'.
# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary.

rivers = {
    'fiume azzuro': 'cina',
    'mississippi': 'usa',
    'purus': 'brasile',
    'indo': 'pakistan',
    'mekong': 'laos'
}

# key and value
print("\nList of famous rivers:")
for key, value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}.")

# only the key
print("\nRivers:")
for key in rivers:
    print(key.title()) 

# only the value
print("\nCountries:")
for value in rivers.values():
    print(value.title())



print()
# 6-6. Polling: Use the code in favorite_languages.py (page 97).
# Make a list of people who should take the favorite languages poll. 
# Include some names that are already in the dictionary and some that
# are not.
# Loop through the list of people who should take the poll. 
# If they have already taken the poll, print a message thanking them for responding. 
# If they have not yet taken the poll, print a message inviting them to take the poll.
fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'renato': 'C',
    'ainhoa': 'CSS',
    'tili': 'ruby',
    'pinxti': 'pascal'
}

completed = ['jen', 'sarah', 'edward', 'phil']

for name, language in fav_languages.items():
    if name in completed:
        print(f"Thank you {name.title()} for responding.")
    else:
        print(f"Hello {name.title()}, your favourite languange is {language.title()}, very good!")
