# 10-3. Guest: Write a program that prompts the user for their name. 
# When they respond, write their name to a file called guest.txt.
filename = 'test_files/guests.txt'

name = input("Please enter your name: ")

with open(filename, 'w') as file_objects:
    file_objects.write(f'{name.title()}\n')




# 10-4. Guest Book: Write a while loop that prompts users for their 
# name. When they enter their name, print a greeting to the screen and
# add a line recording their visit in a file called guest_book.txt. 
# Make sure each entry appears on a new line in the file.
filepath = 'test_files/guest_book.txt'
ask = True

while ask:
    ask = input("Welcome. Please enter your name: ")
    with open(filepath, 'a') as file_object:
        file_object.write(f"{ask.title()}\n")







# 10-5. Programming Poll: Write a while loop that asks people why they 
# like programming. Each time someone enters a reason, add their reason
# to a file that stores all the responses.
# I'll change it a bit

filefile = 'test_files/poll.txt'
message = True

while message:
    message = input("List your favourite fruits: ")
    with open(filefile, 'a') as file_object:
        file_object.write(f"{message}\n")
