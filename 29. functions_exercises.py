# 8-12. Sandwiches: Write a function that accepts a list of items a 
# person wants on a sandwich. The function should have one parameter
# that collects as many items as the function call provides, and it
# should print a summary of the sandwich that’s being ordered. 
# Call the function three times, using a different number of arguments
# each time.

def make_sandwich(*items):
    if len(items) > 1:
        qnt = 'items'
    else:
        qnt = 'item'
    print(f"Making a sandwich with the following {qnt}:")
    
    for item in items:
        print(f"- {item}")

make_sandwich('tomatoes', 'avocado', 'tuna', 'mayonnaise')
print()
make_sandwich('eggs', 'mayonnaise')
print()
make_sandwich('ham')




# 8-13. User Profile: Start with a copy of user_profile.py from page 149.
# Build a profile of yourself by calling build_profile(), using your 
# first and last names and three other key-value pairs that describe you.
def build_profile(first, last, **user_info):
    user_info['name'] = first
    user_info['surname'] = last

    return user_info


user_profile = build_profile('renato', 'bianco', city='cork', country='ireland')

print("Printing details of the current user:")

for value in reversed(user_profile.values()):
    print(f"- {value.title()}")





# 8-14. Cars: Write a function that stores information about a car in a
# dictionary. The function should always receive a manufacturer and a 
# model name. It should then accept an arbitrary number of keyword 
# arguments. Call the function with the required information and two
# other name-value pairs, such as a color or an optional feature. Your
# function should work for a call like this one:
#
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
#
# Print the dictionary that’s returned to make sure all the information
# was stored correctly.
def car_info(manufacturer, model_name, **car_details):
    car_details['manufacturer'] = manufacturer
    car_details['model_name'] = model_name
    
    return car_details

my_car = car_info('Ford', 'Raptor', color='black', year=2021, tow_package=True)

print(my_car)




# repeating 8-13 as it should have done, probably...
def my_self(name, surname, age, city):
    full_details = f"\n{name.title()} {surname.title()} is {age} years old and lives in {city.title()}.\n"
    print(full_details)

description = my_self('renato', 'bianco', age=42, city='cork')
