user = {
    'username': 'renato79',
    'firstn': 'renato',
    'lastn': 'bianco'
}

for key, value in user.items():
    print(f"{key.title()}: {value.title()}")



fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print()

# These descriptive names, name and language, make it much easier to
# see what the print() call is doing.
for name,language in fav_languages.items():
    print(f"{name.title()}'s favourite language is: {language.title()}.")

print()


# The keys() method is useful when you don’t need to work with all of 
# the values in a dictionary.
for name in fav_languages.keys():
    print(name.title())
# Looping through the keys is actually the default behavior when looping
# through a dictionary, so this code would have exactly the same output 
# if you wrote:
for name in fav_languages:
    print(name.title())
# You can choose to use the keys() method explicitly if it makes your
# code easier to read, or you can omit it if you wish.



friends = ['jen', 'phil']

for name in fav_languages:
    print(f"Hello {name.title()}!")
    
    if name in friends:
        language = fav_languages[name].title()
        print(f"\t{name.title()}, I see you like {language}!")
    
if 'erin' not in friends:
    print("Erin, please take our poll!")
    

print()



for name in sorted(fav_languages):
    print(name.title())

print(fav_languages)




# If you are primarily interested in the values that a dictionary 
# contains, you can use the values() method to return a list of values 
# without any keys. For example, say we simply want a list of all 
# languages chosen in our programming language poll without the name
# of the person who chose each language:
for language in fav_languages.values():
    print(f"Language: {language.title()}\n")



# When you wrap set() around a list that contains duplicate items, Python
# identifies the unique items in the list and builds a set from those items.
print(set(fav_languages.values()))
# OR
for value in set(fav_languages.values()):
    print(value)



###   ## 
## #  ##
##  # ##
##   ### OTE

# NOTE: You can build a set directly using braces and separating the elements with commas:
languages = {'python', 'ruby', 'python', 'c', 'ruby', 'python'}

print(languages) # result: {'c', 'ruby', 'python'}

for i in languages:
    print(i) # result: c ruby python (each on a new line)
# When you see braces but no key-value pairs, you’re probably looking 
# at a set. Unlike lists and dictionaries, sets do not retain items in
# any specific order.