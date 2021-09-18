# Counting
num = 1

while num <= 5:
    print(num)
    num += 1


# Quit
message = ""

while message != 'quit':
    message = input("\nType quit to end the program: ")



# For a program that should run only as long as many conditions are 
# true, you can define one variable that determines whether or not the 
# entire program is active.

# This variable, called a flag, acts as a signal to the program.
prompt = "\nTell my something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program: "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)


# Using break

prompt = "\nEnter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you have finished.)"
prompt += "\n: "

# A loop that starts with while True will run forever unless it reaches
# a break statement.
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")



# Using continue

a = 0

while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)




# A for loop is effective for looping through a list, but you shouldn’t 
# modify a list inside a for loop because Python will have trouble 
# keeping track of the items in the list. To modify a list as you work 
# through it, use a while loop. Using while loops with lists and 
# dictionaries allows you to collect, store, and organize lots of input
# to examine and report on later.

# Moving Items from One List to Another

unconf_users = ['renato', 'ainhoa', 'tili', 'pintxi']
conf_users = []

while unconf_users:
    user = unconf_users.pop()
    
    print(f"\nConfirming user {user.title()}...")
    print("Confirmed, adding to the list...")
    conf_users.append(user)
    
print("\nUsers correctly confirmed:")
for user in conf_users:
    print(user.title())




# Removing All Instances of Specific Values from a List
# remove()
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)




# Filling a Dictionary with User Input
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    mountain = input("Which mountain would you like to climb someday? ")
    
    responses[name] = mountain
    
    repeat = input("\nWould you like to let another person respond? ")
    
    if repeat == 'no':
        polling_active = False
    
print("\n\t--- Poll Results ---")

for name, response in responses.items():
    print(f"{name.title()} would like to climb the {response.title()}")