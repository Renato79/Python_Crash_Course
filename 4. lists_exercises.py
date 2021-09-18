# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
# Make a list that includes at least three people you’d like to invite to dinner. 
# Then use your list to print a message to each person, inviting them to dinner.

guests = ['tom', 'jerry', 'spencer', 'ami', 'patty']

print()
print(f"An invitation has been sent for {guests[0].title()}.")
print(f"An invitation has been sent for {guests[1].title()}.")
print(f"An invitation has been sent for {guests[2].title()}.")
print(f"An invitation has been sent for {guests[3].title()}.")
print(f"An invitation has been sent for {guests[4].title()}.")
print()


# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need 
# to send out a new set of invitations. You’ll have to think of someone else to invite.
# Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name 
# of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.

print(f"I'm sorry to inform you that {guests[3].title()} won't be with us for dinner.")

guests.pop(3)
guests.insert(3, 'carol')
# guests[3] = 'carol'

print()

for a in guests:
    print(f"A new invitation has been sent to {a.title()}.")

print()


# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. 
# Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing 
# people that you found a bigger dinner table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

print("I'm glad to inform that I found a bigger table for our dinner.")

guests.insert(0, 'mike')
guests.insert(3, 'jack')
guests.append('doris')

print()

for b in guests:
    print(f"A new invitation has been sent to {b.title()} for a dinner at a bigger table.")

print()


# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, 
# and you have space for only two guests.
# Start with your program from Exercise 3-6. Add a new line that prints a message saying that 
# you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. 
# Each time you pop a name from your list, print a message to that person letting them know 
# you’re sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty list. 
# Print your list to make sure you actually have an empty list at the end of your program.

print("I'm sorry to inform all the guests that due to a delay, we can only invite two people for dinner.")
print()

num = len(guests)

while num > 2:
    name = guests.pop()
    print(f"I'm sorry but {name.title()} cannot come for dinner due to a delay with the table availability.")
    num = num - 1

print()
print(f"A new invitation has been sent to {guests[0].title()} since there is space for two.")
print(f"A new invitation has been sent to {guests[1].title()} since there is space for two.")
print()

del guests[0]
del guests[0]

print(guests)
print()