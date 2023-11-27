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

class AboutSequenceTypes(unittest.TestCase):
    def test_create_list(self):
        string_list = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"]
        self.assertGreaterEqual(len(string_list), 4, "You must enter at least four strings inside the square brackets.")
        for item in string_list:
            self.assertGreaterEqual(len(item), 4, "Each string in the list must have at least four characters.")

    def test_create_tuple(self):
        my_tuple = ("Pet Sounds", "Revolver", "Evolution", "Headquarters")
        self.assertGreaterEqual(len(my_tuple), 4, "You must enter at least four strings inside the parentheses.")
        for item in my_tuple:
            self.assertGreaterEqual(len(item), 4, "Each string in the tuple must have at least four characters.")

    def test_create_range(self):
        numbers = range(5)
        self.assertEqual(True, isinstance(numbers, range))

class AboutMappingType(unittest. TestCase):
    def test_dictionary(self):
        song = {"title": "Tomorrow Never Knows", "songwriter(s)": "Lennon-McCartney", "album": "Revolver", "artist": "The Beatles"}
        self.assertGreaterEqual(len(song), 4, "You must enter at least four strings inside the curly brackets.")

class AboutSetTypes(unittest.TestCase):
    def test_set(self):
        subjects = {"Programming", "Business", "Economics", "Law", "Psychology", "History"}
        self.assertEqual(True, isinstance(subjects, set))
    
    def test_frozenset(self):
        movies = frozenset({"Picture Snatcher", "Casablanca", "Singin' in the Rain", "The Sound of Music", "The Godfather", "The Breakfast Club", "L.A. Confidential", "Casino Royale", "The Hateful Eight"})
        self.assertEqual(True, isinstance(movies, frozenset))

class AboutBooleanType(unittest.TestCase):
    def test_boolean(self):
        x = True
        self.assertTrue(True, isinstance(x, bool))

    def test_boolean_false(self):
        y = False
        self.assertFalse(False, isinstance(y, bool))

class AboutBinaryTypes(unittest.TestCase):
    def test_bytes(self):
        binary_test1 = b"Hello, world!"
        self.assertEqual(True, isinstance(binary_test1, bytes))

    def test_bytearray(self):
        binary_test2 = bytearray(5)
        self.assertEqual(True, isinstance(binary_test2, bytearray))
    
    def test_memoryview(self):
        binary_test3 = memoryview(bytes(3))
        self.assertEqual(True, isinstance(binary_test3, memoryview))

class AboutNoneType(unittest.TestCase):
    def test_none(self):
        x = None
        self.assertIsNone(x)

#class AboutArithmeticOperators(unittest.TestCase):

if __name__ == '__main__':
    unittest.main()