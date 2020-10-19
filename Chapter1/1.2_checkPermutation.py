"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
"""


def solution_using_sorting(str1, str2):
    """
    Determines whether one string is permutation of other string or not
    :param str1: First string
    :param str2: Second string
    :return: True/False
    """
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if sorted_str1 == sorted_str2:
        return True
    return False


def solution_using_unicode(str1, str2):
    """
    Determines whether one string is permutation of other string or not
    :param str1: First string
    :param str2: Second string
    :return: True/False
    """
    NO_OF_CHARS = 256
    count1 = [0]*NO_OF_CHARS
    count2 = [0]*NO_OF_CHARS
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        count1[ord(str1[i])] += 1
        count2[ord(str2[i])] += 1
    for i in range(NO_OF_CHARS):
        if count1[i] != count2[i]:
            return False
    return True


def solution_using_single_unicode(str1, str2):
    """
    Determines whether one string is permutation of other string or not
    :param str1: First string
    :param str2: Second string
    :return: True/False
    """
    NO_OF_CHARS = 256
    count = [0] * NO_OF_CHARS
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        count[ord(str1[i])] += 1
        count[ord(str2[i])] -= 1
    for i in range(NO_OF_CHARS):
        if count[i] != 0:
            return False
    return True


if __name__ == '__main__':
    s1 = "namita"
    s2 = "tamina"

    if solution_using_sorting(s1, s2):
        print("'{}' is permutation of '{}'".format(s1, s2))
    else:
        print("'{}' is not a permutation of '{}'".format(s1, s2))

    if solution_using_unicode(s1, s2):
        print("'{}' is permutation of '{}'".format(s1, s2))
    else:
        print("'{}' is not a permutation of '{}'".format(s1, s2))

    if solution_using_single_unicode(s1, s2):
        print("'{}' is permutation of '{}'".format(s1, s2))
    else:
        print("'{}' is not a permutation of '{}'".format(s1, s2))
