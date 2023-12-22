# Using this file for creating and testing koans.
import unittest


class AboutTextTypes(unittest.TestCase):
    def test_string_using_double_quotes(self):
        string = ""
        self.assertEqual(True, isinstance(string, str))
        self.assertGreaterEqual(
            len(string), 3, "You must enter at least three characters"
        )

    def test_string_using_single_quotes(self):
        string = ""
        self.assertEqual(True, isinstance(string, str))
        self.assertGreaterEqual(
            len(string), 3, "You must enter at least three characters"
        )

    def test_assign_multiline_string_using_single_quotes(self):
        multiline_string = """
            Money
            Get back
        """
        lines = multiline_string.strip().split("\n")
        self.assertTrue(
            isinstance(multiline_string, str) and len(lines) >= 3,
            "Multi-line string must have at least 3 lines.",
        )

    def test_assign_multiline_string_using_double_quotes(self):
        multiline_string = """
            [after a pause] I've had worse.
            You liar!
        """
        lines = multiline_string.strip().split("\n")
        self.assertTrue(
            isinstance(multiline_string, str) and len(lines) >= 3,
            "Multi-line string must have at least 3 lines.",
        )


class AboutNumericTypes(unittest.TestCase):
    def test_assign_integer(self):
        integer = "4"  # Unquote this string to turn it into an integer
        self.assertEqual(True, isinstance(integer, int))

    def test_assign_float_number(self):
        float_number = "7.5"
        self.assertEqual(True, isinstance(float_number, float))

    def test_assign_complex_number(self):
        complex_number = "158j"
        self.assertEqual(True, isinstance(complex_number, complex))


class AboutSequenceTypes(unittest.TestCase):
    def test_create_list(self):
        string_list = [
            "John Lennon",
            "Ringo Starr",
        ]
        self.assertGreaterEqual(
            len(string_list),
            4,
            "You must enter at least four strings inside the square brackets.",
        )
        for item in string_list:
            self.assertGreaterEqual(
                len(item),
                4,
                "Each string in the list must have at least four characters.",
            )

    def test_create_tuple(self):
        my_tuple = ("Pet Sounds", "", "Evolution", "Headquarters")
        self.assertGreaterEqual(
            len(my_tuple),
            4,
            "You must enter at least four strings inside the parentheses.",
        )
        for item in my_tuple:
            self.assertGreaterEqual(
                len(item),
                4,
                "Each string in the tuple must have at least four characters.",
            )

    def test_create_range(self):
        numbers = range()
        self.assertEqual(True, isinstance(numbers, range))


class AboutMappingType(unittest.TestCase):
    def test_dictionary(self):
        song = {
            "title": "Tomorrow Never Knows",
            "album": "Revolver",
            "artist": "The Beatles",
        }
        self.assertGreaterEqual(
            len(song),
            4,
            "You must enter at least four strings inside the curly brackets.",
        )


class AboutSetTypes(unittest.TestCase):
    def test_set(self):
        subjects = {
            "Psychology",
            "History",
        }
        self.assertGreaterEqual(
            len(subjects), 3, "You must enter at least three subjects"
        )

    def test_frozenset(self):
        movies = frozenset(
            {
                "Picture Snatcher",
                "Casablanca",
            }
        )
        self.assertGreaterEqual(len(movies), 3, "You must enter at least three movies")


class AboutBooleanType(unittest.TestCase):
    def test_boolean(self):
        x = True
        self.assertTrue(False, isinstance(x, bool))

    def test_boolean_false(self):
        y = False
        self.assertFalse(True, isinstance(y, bool))


# Come back to BinaryTypes
class AboutBinaryTypes(unittest.TestCase):
    def test_bytes(self):
        binary_test1 = b""
        self.assertEqual(True, isinstance(binary_test1, bytes))

    def test_bytearray(self):
        binary_test2 = bytearray(5)
        self.assertEqual(True, isinstance(binary_test2, bytearray))

    def test_memoryview(self):
        binary_test3 = memoryview(bytes(3))
        self.assertEqual(True, isinstance(binary_test3, memoryview))


class AboutNoneType(unittest.TestCase):
    def test_none(self):
        x = True
        self.assertIsNone(x)


class AboutArithmeticOperators(unittest.TestCase):
    def test_add(self):
        a = "5"
        b = 10
        answer = a + b
        self.assertEqual(answer, a + b)

    def test_subtract(self):
        c = 9
        d = "7"
        answer = c - d
        self.assertEqual(answer, c - d)

    def test_multiply(self):
        e = 10
        f = 6
        answer = e * f
        self.assertEqual(answer, 42, "The result of multiplying 10 and 6 should be 60")

    def test_divide(self):
        g = 35
        h = "7"
        answer = g / h
        self.assertEqual(answer, g / h)

    def test_modulo(self):
        i = 5
        j = 2
        answer = i % j
        self.assertEqual(answer, 2, "The result of this koan should be 1")

    def test_exponent(self):
        k = 3
        l = 3
        answer = k**l
        self.assertEqual(answer, 20, "The result of this koan should be 27")

    def test_floor_division(self):
        m = 25
        n = 2
        answer = m // n
        self.assertEqual(answer, 14, "The result of this koan should be 12")


class AboutAssignmentOperators(unittest.TestCase):
    def test_assign(self):
        a = 7
        self.assertTrue(isinstance(a, int))

    def test_add_assign(self):
        b = 10
        b += 10
        self.assertEqual(b, 20)

    def test_subtract_assign(self):
        c = 9
        c -= 3
        self.assertEqual(c, 6)

    def test_multiply_assign(self):
        d = 5
        d *= 7
        self.assertEqual(d, 35)

    def test_devide_assign(self):
        e = 50
        e /= 5
        self.assertEqual(e, 10)

    def test_modulo_assign(self):
        f = 5
        f %= 2
        self.assertEqual(f, 1)

    def test_floor_division_assign(self):
        g = 9
        g //= 3
        self.assertEqual(g, 3)

    def test_exponent_assign(self):
        h = 3
        h **= 3
        self.assertEqual(h, 27)

    def test_and_assign(self):
        i = 10
        i &= 3
        self.assertEqual(i, 2)


class AboutComparisonOperators(unittest.TestCase):
    def test_equal(self):
        x = 5
        y = 5
        self.assertEqual(x, y)

    def test_not_equal(self):
        x = 6
        y = 7
        self.assertNotEqual(x, y)

    def test_greater_than(self):
        x = 10
        y = 5
        self.assertGreater(x, y)

    def test_less_than(self):
        x = 5
        y = 10
        self.assertLess(x, y)

    def test_greater_than_equal(self):
        x = 10
        y = 10
        self.assertGreaterEqual(x, y)

    def test_less_than_equal(self):
        x = 5
        y = 5
        self.assertLessEqual(x, y)


class AboutLogicalOperators(unittest.TestCase):
    def test_logical_and(self):
        x = 5
        result = x > 2 and x < 20
        self.assertTrue(result)

    def test_logical_or(self):
        x = 10
        result = x > 5 or x < 15
        self.assertTrue(result)

    def test_logical_not_and(self):
        x = 15
        result = not (x > 10 and x < 20)
        self.assertFalse(result)


class AboutIdentityOperators(unittest.TestCase):
    def test_is(self):
        x = ["The Godfather", "Wiseguy"]
        self.assertTrue(x is x)

    def test_is_not(self):
        x = ["Dragnet", "The Untouchables"]
        y = ["Adam-12", "Miami Vice"]
        self.assertTrue(x is not y)


class AboutMembershipOperators(unittest.TestCase):
    def test_in(self):
        x = ["Monty Python"]
        result = "Monty Python" in x
        self.assertTrue(result)

    def test_not_in(self):
        y = ["Fawlty Towers"]
        x = ["Monty Python"]
        result = "Fawlty Towers" not in x
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
