"""
Write a method to replace all spaces in a string with '%20: You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith "
Output: "Mr%20John%20Smith"
"""
MAX = 1000


def solution(str1):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    :param str1: inout string
    :return: URLfied string
    """
    str1 = str1.strip()
    n = len(str1)
    spaces = str1.count(' ')
    new_length = n + spaces*2

    if new_length > MAX:
        return -1

    index = new_length - 1
    str1 = list(str1)

    for f in range(n, new_length):
        str1.append('0')
    # Fill rest of the string from end
    for j in range(n - 1, 0, -1):

        # inserts %20 in place of space
        if str1[j] == ' ':
            str1[index] = '0'
            str1[index - 1] = '2'
            str1[index - 2] = '%'
            index = index - 3
        else:
            str1[index] = str1[j]
            index -= 1

    return ''.join(str1)


if __name__ == '__main__':
    print(solution('Mr John Smith'))