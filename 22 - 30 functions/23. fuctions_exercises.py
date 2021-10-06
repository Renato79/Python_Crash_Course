# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size
# and the text of a message that should be printed on the shirt. 
# The function should print a sentence summarizing the size of the 
# shirt and the message printed on it.
#
# Call the function once using positional arguments to make a shirt. 
# Call the function a second time using keyword arguments.

def make_shirt(size, text):
    print(f"\nThe t-shirt size is {size.upper()}.")
    print(f"Message to print on the t-shirt: {text}")

make_shirt('xl', 'I\'m just rebooting')

make_shirt(size='l', text='Toto, I\'ve a feeling we\'re not in Kansas anymore.\n')



# 8-4. Large Shirts: Modify the make_shirt() function so that shirts
# are large by default with a message that reads I love Python. Make
# a large shirt and a medium shirt with the default message, and a 
# shirt of any size with a different message.
def create_tshirt(size='l', text='i love python'):
    print(f"\nThe t-shirt size is {size.upper()}.")
    print(f"Message to print on the t-shirt: {text.title()}\n")

create_tshirt()
create_tshirt(size='m')
create_tshirt(size='xl', text='more zen')




# 8-5. Cities: Write a function called describe_city() that accepts the
# name of a city and its country. The function should print a simple 
# sentence, such as Reykjavik is in Iceland. Give the parameter for the
# country a default value. Call your function for three different cities,
# at least one of which is not in the default country.
def describe_city(city, country='italy'):
    print(f"{city.title()} is in {country.title()}.")

describe_city('rome')
describe_city('london', 'england')
describe_city('torino')
describe_city(city='paris', country='france')

# The following generates an error
# SyntaxError: Positional argument cannot appear after keyword arguments
# describe_city(city='amsterdam', 'the netherland')