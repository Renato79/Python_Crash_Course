# Create a file called test_cities.py that tests the function you just
# wrote (remember that you need to import unittest and the function you
# want to test). Write a method called test_city_country() to verify 
# that calling your function with values such as 'santiago' and 'chile'
# results in the correct string. Run test_cities.py, and make sure
# test_city_country() passes.
import unittest

from main import format_country

class TestFormatCountry(unittest.TestCase):
    
    def test_format_country(self):
        """Testing the function in main.py"""
        complete_address = format_country('cork', 'ireland')
        self.assertEqual(complete_address, 'Cork, Ireland.')

if __name__ == '__main__':
    unittest.main()