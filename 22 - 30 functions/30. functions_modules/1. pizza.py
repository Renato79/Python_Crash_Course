# Importing an Entire Module
#
# When Python reads this file, the line import pizza tells Python to 
# open the file pizza.py and copy all the functions from it into this
# program.
# This makes every function from the module available in your program
import make_module # make_module.py

# To call a function from an imported module, enter the name of the 
# module you imported, pizza, followed by the name of the function,
# make_pizza(), separated by a dot.
make_module.make_pizza(16, 'pomodoro', 'prosciutto', 'funghi')
make_module.make_pizza(12, 'pomodoro', 'origano')