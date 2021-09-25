# Using as to Give a Function an Alias
#
# If the name of a function you’re importing might conflict with an 
# existing name in your program or if the function name is long, you
# can use a short, unique alias—an alternate name similar to a nickname
# for the function. You’ll give the function this special nickname when
# you import the function.

# Here we give the function make_pizza() an alias, mp(), by importing 
# make_pizza as mp. The as keyword renames a function using the alias
# you provide:
from make_module_2 import make_panuozzo as mp


mp(50, 'mozzarella', 'prosciutto', 'funghi')