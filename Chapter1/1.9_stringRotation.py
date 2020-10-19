"""
String Rotation: Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, S1 and S2, write code to check if S2 is a rotation of S1 using only one
call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").
"""
import unittest


def isSubstring(s1, s2):
    return s2.find(s1) != -1


def solve(s1, s2):
    """
    Time Complexity : O(N)
    Space Complexity : O(1)
    :param s1: Input 1
    :param s2: Input 2
    :return: Boolean
    """
    return isSubstring(s2, s1+s1)


class Test(unittest.TestCase):
    data = [("waterbottle", "erbottlewat", True),
            ("waterbottles", "erbottlewat", False),
            ("foo", "foofoo", True)]

    def test_is_string_rotation(self):
        for test_string1, test_string2, expected_output in self.data:
            actual = solve(test_string1, test_string2)
            self.assertEqual(actual, expected_output)


if __name__ == '__main__':
    unittest.main()