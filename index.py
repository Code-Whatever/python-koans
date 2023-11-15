# Using this file for creating and testing koans.
import unittest

class AboutDataTypes(unittest.TestCase):
    def test_string_using_double_quotes(self):
        string = "spam"
        self.assertEqual(True, isinstance(string, str))

    def test_string_using_single_quotes(self):
        string = 'eggs'
        self.assertEqual(True, isinstance(string, str))
    
    #def test_assign_multiline_string_using_single_quotes(self):

    def test_assign_value_to_variable(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()