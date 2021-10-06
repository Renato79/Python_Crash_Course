# 8-7. Album: Write a function called make_album() that builds a 
# dictionary describing a music album. The function should take in an
# artist name and an album title, and it should return a dictionary 
# containing these two pieces of information. Use the function to make
# three dictionaries representing different albums. Print each return
# value to show that the dictionaries are storing the album information
# correctly.

# Use None to add an optional parameter to make_album() that allows you
# to store the number of songs on an album. If the calling line includes 
# a value for the number of songs, add that value to the album’s 
# dictionary. Make at least one new function call that includes the 
# number of songs on an album.

def make_album(artist_name, album_title, songs=None):
    album = {'artist_name': artist_name, 'album_title': album_title}
    
    if songs:
        album['songs'] = songs

    return album

my_album = make_album(artist_name='pink floyd', album_title='the wall')
print(my_album)

my_album = make_album('nirvana', 'nevermind')
print(my_album)

my_album = make_album('queen', 'rock in rio')
print(my_album)

my_album = make_album('boyce avanue', 'collection', 18)
print(my_album)


# 8-6. City Names: Write a function called city_country() that takes in
# the name of a city and its country. The function should return a string
# formatted like this:
#
# "Santiago, Chile"
#
# Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(city, country):
    place = f"{city}, {country}"
    
    return place.title()

city_1 = city_country('rome', 'italy')
city_2 = city_country('paris', 'france')
city_3 = city_country('tokyo', 'japan')

print(city_1)
print(city_2)
print(city_3)



# 8-8. User Albums: Start with your program from Exercise 8-7. Write a
# while loop that allows users to enter an album’s artist and title. 
# Once you have that information, call make_album() with the user’s input
# and print the dictionary that’s created. 
# Be sure to include a quit value in the while loop.


print("\nLet's create dictionaries!\n(enter quit to exit)\n")
while True:
    band = input('\nBand: ')
    if band == 'quit':
        break
    
    album = input('Album: ')
    if album == 'quit':
        break

    my_album = make_album(band, album)
    
    print(my_album)
    