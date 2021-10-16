import os

from bills import Bills
from products import Products


os.system('clear')

print("\nHello! My name is Data, and I will check things for you.")
print("Please tell me what would you like me to check:\n\n")
# List of options:
print("1. Bills to pay")
print("2. Products availability")

# Getting the input from the user:
while True:
    option = input("\n\n> ")

    if option == '1':
        bills = Bills('home')
        bills.check_gas()
        bills.check_el()
    elif option == '2':
        products = Products('home')
        products.check_paper()
        products.check_water()
        products.delivery.check_delivery()
    elif option == 'q':
        print("\nExiting, goodbye.\n\n")
        break