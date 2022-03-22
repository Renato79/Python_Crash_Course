# Testing a Function
"""
def get_formatted_name(first, last):
    return f"{first} {last}".title()
"""

# Testing a Function to make the test fail
def get_formatted_name(first, last, middle=''):
    if middle:
        return f"{first} {middle} {last}".title()
    else:
        return f"{first} {last}".title()