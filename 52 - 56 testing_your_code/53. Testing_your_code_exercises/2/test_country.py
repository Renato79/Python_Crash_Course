import unittest

from main import format_country

class TestCountry(unittest.TestCase):
    """Test the function format_country in main.py"""

    def test_format_country(self):
        country = format_country('cork', 'ireland')
        self.assertEqual(country, 'Cork, Ireland.')
    
    def test_format_country_with_population(self):
        country = format_country('cork', 'ireland', '500000')
        self.assertEqual(country, 'Cork, Ireland – Population 500000.')
        
if __name__ == '__main__':
    unittest.main()