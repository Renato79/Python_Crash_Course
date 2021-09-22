# You’ll often find it useful to pass a list to a function, whether 
# it’s a list of names, numbers, or more complex objects, such as dictionaries. 
def greet_users(names):
    for name in names:
        msg = f"Hello {name.title()}!"
        print(msg)

names = ['renato', 'ainhoa', 'tili', 'pintxi']

greet_users(names)

print()



# This example also demonstrates the idea that every function should 
# have one specific job. The first function prints each design, and the
# second displays the completed models. This is more beneficial than 
# using one function to do both jobs. If you’re writing a function and
# notice the function is doing too many different tasks, try to split
# the code into two functions. Remember that you can always call a 
# function from another function, which can be helpful when splitting
# a complex task into a series of steps.
def printing(pending, completed):
    while pending:
        send = pending.pop()
        print(f"Printing a {send}...")
        completed.append(send)
        
    return completed

def show_completed(completed):
    print("\nLet's see what we have printed so far:")
    
    for printed in completed:
        print(printed.title())


models_to_print = ['tree', 'robot', 'phone case', 'vase', 'spoon']
completed_prints = []

models_completed = printing(models_to_print, completed_prints)
show_completed(models_completed)
    