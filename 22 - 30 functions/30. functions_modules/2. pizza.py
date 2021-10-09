# Importing Specific Functions
# You can also import a specific function from a module. Here’s the 
# general syntax for this approach:
from make_module_2 import make_panuozzo

# You can import as many functions as you want from a module by 
# separating each function’s name with a comma:
#
# from module_name.py import function_0, function_1, function_2

# With this syntax, you don’t need to use the dot notation when you call
# a function. Because we’ve explicitly imported the function make_pizza()
# in the import statement, we can call it by name when we use the function.
make_panuozzo(50, 'mozzarella', 'prosciutto', 'funghi')