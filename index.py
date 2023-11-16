# Using this file for creating and testing koans.
import unittest

class AboutTextTypes(unittest.TestCase):
    def test_string_using_double_quotes(self):
        string = "spam"
        self.assertEqual(True, isinstance(string, str))
        self.assertGreaterEqual(len(string), 3, "You must enter at least three characters")

    def test_string_using_single_quotes(self):
        string = 'eggs'
        self.assertEqual(True, isinstance(string, str))
        self.assertGreaterEqual(len(string), 3, "You must enter at least three characters")

    def test_assign_multiline_string_using_single_quotes(self):
        multiline_string = '''
            Money
            Get back
            I'm alright, Jack, keep your hands off of my stack
        '''
        lines = multiline_string.strip().split('\n')
        self.assertTrue(isinstance(multiline_string, str) and len(lines) >= 3, "Multi-line string must have at least 3 lines.")

    def test_assign_multiline_string_using_double_quotes(self):
        multiline_string = """
            Now stand aside, worthy adversary!
            'Tis but a scratch!
            A scratch? Your arm's off!
            No, it isn't.
            Well what's that, then?
            [after a pause] I've had worse.
            You liar!
        """
        lines = multiline_string.strip().split('\n')
        self.assertTrue(isinstance(multiline_string, str) and len(lines) >= 3, "Multi-line string must have at least 3 lines.")

class AboutNumericTypes(unittest.TestCase):
    def test_assign_integer(self):
        integer = 5
        self.assertEqual(True, isinstance(integer, int))

    def test_assign_float_number(self):
        float_number = 64.8
        self.assertEqual(True, isinstance(float_number, float))

    def test_assign_complex_number(self):
        complex_number = 158j
        self.assertEqual(True, isinstance(complex_number, complex))

class AboutSquenceTypes(unittest.TestCase):
    def test_create_string_list(self):
        string_list = ["John Lennon", "Paul McCartney", "George Harrison"]
        self.assertEqual(True, isinstance(string_list, list))
        self.assertGreater(len(string_list), 2, "List is empty. You must enter three strings inside the square brackets.")

if __name__ == '__main__':
    unittest.main()