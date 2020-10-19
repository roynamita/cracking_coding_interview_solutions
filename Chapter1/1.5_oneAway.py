"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales. pale -> true
pale. bale -> true
pale. bake -> false
"""


def solution(str1, str2):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    :param str1:
    :param str2:
    :return: Boolean
    """
    m = len(str1)
    n = len(str2)

    # If difference in length of both strings are more than 1 then return False
    if abs(m-n) > 1:
        return False
    i = 0
    j = 0
    count = 0
    while i < m and j < n:
        if str1[i] != str2[j]:
            # increment the count if strings doesn't match
            count += 1
            # Return false if count is more than 1, as only one edit is needed
            if count > 1:
                return False

            # increment the longer string
            if m > n:
                i += 1
            elif m < n:
                j += 1
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1

    # increment the count if not reached end of string
    if i < m or j < n:
        count += 1
    if count > 1:
        return False
    return True


if __name__ == '__main__':
    print(solution("pale", "ple"))
    print(solution("pales", "pale"))
    print(solution("pale", "bale"))
    print(solution("pale", "bake"))

