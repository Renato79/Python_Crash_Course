# Parrot
message = input("I'm a parrot, write something and I will repeat: ")
print(message)

#1 Greeter
name = input("Please enter your name: ")
print(f"Hello {name.title()}!")

#2 Greater with multilines
prompt = "\nIf you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)

print(f"\nHello, {name.title()}!")


#3 When you use the input() function, Python interprets everything the
# user enters as a string. Consider the following interpreter session, 
# which asks for the user’s age:
age = input("How old are you? ")
print(f"Your age is: {age}")
# The number entered is a string not an int, cannot be used like age >= 18, since it's a string


# Using int() to Accept Numerical Input
age = int(age)
if age >= 18:
    print("You are adult since you are more than 18 y/o.")
else:
    print(f"You are underage since you are only {age} years old.")



#4 The Modulo Operator
number = input("Please enter a number: ")
number = int(number)

if number % 2 == 0:
    print("You've entered a even number.")
else:
    print("You've entered a odd number.")


#5 input inside int() function
number = int(input("How much money do you want in dollars? "))
if number > 50:
    print("You are asking for too much money!")
else:
    print("Ok it's a reasonable amount.")