# import the entire module
import make_module

# from this module, import this function
from make_module_2 import make_panuozzo

# from this module, import this function and refer to the function using the alias 'mp'
from make_module_2 import make_panuozzo as mp

#import this module, and refer to this module using the alias 'pan'
import make_module_2 as pan

# You can import every function in a module by using the asterisk (*) operator.
# It’s best not to use this approach when you’re working with larger modules.
# The best approach is to import the function or functions you want, or import
# the entire module and use the dot notation. This leads to clear code that’s
# easy to read and understand.
from make_module import *



# function calls, using the function make_panuozzo() from the module make_module
make_module.make_panuozzo()

# Calling the function make_panuozzo() imported from make_module_2
make_panuozzo()

# using the alias created for the function make_panuozzo()
mp()

# using pan as alias of the module make_module_2 
pan.make_panuozzo()

# from make_module import *
# Because every function is imported, you can call each function by 
# name without using the dot notation
make_pizza(16, 'pepperoni')
