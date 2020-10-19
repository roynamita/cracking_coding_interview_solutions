"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""

import unittest

def solve(input):
    """
    Return compressed string
    Time complexity: O(N)
    :param input: string
    :return: string
    """
    n = len(input)
    count = 0
    i = 0
    output = ""
    while i < n:
        if i == n-1 or input[i] != input[i+1]:
            output += input[i] + str(count+1)
            count = 0
        else:
            count += 1
        i += 1
    if len(output) >= len(input):
        return input
    return output


class Test(unittest.TestCase):
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = solve(test_string)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    print(solve("aabcccccaaa"))
    print(solve("abcd"))
    unittest.main()