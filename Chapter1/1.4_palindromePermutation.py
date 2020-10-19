"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Cat
Output: True (permutations: "taco cat". "atco cta". etc.)
"""

from collections import Counter


def solution(strg):
    strg = strg.lower()
    d = Counter(strg)
    count = 0
    for key in d:
        if key != " ":
            count += d[key] % 2
    if count > 1:
        return False
    return True


if __name__ == '__main__':
    s = "Tact Cat"
    if solution(s):
        print("'{}' is a palindrome partition".format(s))
    else:
        print("'{}' is not a palindrome partition".format(s))
