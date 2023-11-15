# Using this file for creating and testing koans.
import unittest

class AboutDataTypes(unittest.TestCase):
    def test_string_using_double_quotes(self):
        string = "spam"
        self.assertEqual(True, isinstance(string, str))
        self.assertGreater(len(string), 3, "String is empty. You must enter at least three characters")

    def test_string_using_single_quotes(self):
        string = 'eggs'
        self.assertEqual(True, isinstance(string, str))
        self.assertGreater(len(string), 3, "String is empty. You must enter at least three characters")

    def test_assign_multiline_string_using_single_quotes(self):
        multiline_string = '''
            Money
            Get back
            I'm alright, Jack, keep your hands off of my stack
        '''
        self.assertEqual(True, isinstance(multiline_string, str))

    def test_assign_multiline_string_using_double_quotes(self):
        multiline_string = """
            Now stand aside, worthy adversary!
            'Tis but a scratch!
            A scratch? Your arm's off!
            No, it isn't.
            What's that, then?
            [after a pause] I've had worse.
            You liar!
        """
        self.assertEqual(True, isinstance(multiline_string, str))

if __name__ == '__main__':
    unittest.main()