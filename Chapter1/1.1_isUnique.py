"""
1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""


# Using Sorting
def solution_using_sorting(str1):
    """
    Time complexity: O(nlog(n)) as we are storing the string
    Space complexity: O(1)
    :param str1: Input string on which we have to find whether all characters are unique or not
    :return: True if all characters are unique else False
    """
    str1 = sorted(str1)
    n = len(str1)
    i = 0

    while i < n-1:
        # if the adjacent elements in a sorted string is equal then return False
        if str1[i] == str1[i+1]:
            return False
        i += 1
    return True


def solution_using_unicode(str1):
    """
    Time Complexity: O(n)
    Space Complexity: O(1) as using array of fixed length
    :param str1: Input string on which we have to find whether all characters are unique or not
    :return: True if all characters are unique else False
    """
    if len(str1) > 256:
        return False

    # list of 0s for unicode character for all 256 characters
    charset = [0]*256
    for i in range(len(str1)):
        # if list index for any character is already set that means
        # the character has duplicate entry in list
        if charset[ord(str1[i])]:
            return False
        charset[ord(str1[i])] = 1

    return True


if __name__ == '__main__':
    s = "sbc"
    if solution_using_sorting(s):
        print("All characters of {} are unique".format(s))
    else:
        print("{} contains duplicate characters".format(s))

    if solution_using_unicode(s):
        print("All characters of {} are unique".format(s))
    else:
        print("{} contains duplicate characters".format(s))