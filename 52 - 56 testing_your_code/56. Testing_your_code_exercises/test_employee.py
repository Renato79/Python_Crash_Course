# Write a test case for Employee. Write two test methods, 
# test_give_default_raise() and test_give_custom_raise(). 
# Use the setUp() method so you don’t have to create a new
# employee instance in each test method. Run your test case,
# and make sure both tests pass.
import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):
    """
    Test the class employee, and function give_raise()
    """
    
    def setUp(self):
        self.increase = Employee('frank', 'castle', 40000)
    
    def test_give_default_raise(self):
        new_salary = self.increase.give_rise()
        self.assertEqual(new_salary, '45000')
        
    def test_give_custom_raise(self):
        new_salary = self.increase.give_rise(10000)
        self.assertEqual(new_salary, '50000')

if __name__ == '__main__':
    unittest.main()
