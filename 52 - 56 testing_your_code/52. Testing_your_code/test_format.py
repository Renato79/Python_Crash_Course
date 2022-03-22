# To write a test case for a function, import the unittest module and 
# the function you want to test. Then create a class that inherits from
# unittest.TestCase, and write a series of methods to test different 
# aspects of your function’s behavior.
#
# Here’s a test case with one method that verifies that the function
# get_formatted_name() works correctly when given a first and last name:
import unittest

from format import get_formatted_name


# You can name the class anything you want, but it’s best to call it 
# something related to the function you’re about to test and to use the
# word Test in the class name. This class must inherit from the class 
# unittest.TestCase so Python knows how to run the tests you write.
class Testing(unittest.TestCase): #inheriting
    """Testing format.py"""

    def test_first_last(self):
        """Do names like 'Janis Joplin' work?"""
        full_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(full_name, 'Janis Joplin')
        
    # We name this new method test_first_last_middle_name(). The method 
    # name must start with test_ so the method runs automatically when 
    # we run test_format.py, and because Python calls them automatically,
    # you’ll never have to write code that calls these methods.

    def test_first_middle_last(self):
        full_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(full_name, 'Wolfgang Amadeus Mozart')

# We’re going to run this file directly, but it’s important to note 
# that many testing frameworks import your test files before running
# them. When a file is imported, the interpreter executes the file as
# it’s being imported. The if block at 28 looks at a special variable,
# __name__, which is set when the program is executed. If this file is
# being run as the main program, the value of __name__ is set to 
# '__main__'. In this case, we call unittest.main(), which runs the 
# test case. When a testing framework imports this file, the value of
# __name__ won’t be '__main__' and this block will not be executed.
if __name__ == '__main__':
    unittest.main()
