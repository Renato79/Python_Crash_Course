# 8-9. Messages: Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), which prints each 
# text message.

def show_messages(messages):       
    for quote in messages.values():
        print(quote)

messages = {
    'message_1': 'Let go, or be dragged.',
    'message_2': 'Do not let the behavior of others destroy your inner peace.',
    'message_3': 'Smile, breathe and go slowly.',
    'message_4': 'Act without expectation.',
    'message_5': 'Do not follow the idea of others, but learn to listen to the voice within yourself.',
    'message_5': 'Fear is a natural reaction to moving closer to the truth.'
}

show_messages(messages)

print()



# 8-11. Archived Messages: Start with your work from Exercise 8-10. 
# Call the function send_messages() with a copy of the list of messages. 
# After calling the function, print both of your lists to show that the 
# original list has retained its messages.


def moving(models, receive):
    while models:
        take = models.pop()
        print(f"Printing {take}")
        receive.append(take)
    return models
    
    



models_to_print = ['tree', 'robot', 'phone case', 'vase', 'spoon']
receiver = []

# The slice notation [:] makes a copy of the list to send to the 
# function.
send = moving(models_to_print[:], receiver)

print(f"Copy: {send}")
print(f"Original: {models_to_print}")

# Even though you can preserve the contents of a list by passing a copy 
# of it to your functions, you should pass the original list to 
# functions unless you have a specific reason to pass a copy. It’s more
# efficient for a function to work with an existing list to avoid using
# the time and memory needed to make a separate copy, especially when 
# you’re working with large lists.