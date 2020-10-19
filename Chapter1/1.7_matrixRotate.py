"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""
import unittest


def solve(matrix):
    """
    Time Complexity : O(N^2)
    Space Complexity : O(1)
    :param matrix:
    :return: rotated matrix
    """
    n = len(matrix)

    for x in range(n//2):
        for y in range(x, n-1-x):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][n-1-x]
            matrix[y][n-1-x] = matrix[n-1-x][n-1-y]
            matrix[n-1-x][n-1-y] = matrix[n-1-y][x]
            matrix[n-1-y][x] = temp

    return matrix


class Test(unittest.TestCase):
    data = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12,
             13, 14, 15, 16]]
    expected = [[4, 8, 12, 16],
                [3, 7, 11, 15],
                [2, 6, 10, 14],
                [1, 5, 9, 13]]

    def rotate_matrix(self):
        actual_mtraix = solve(self.data)
        self.assertEqual(actual_mtraix, self.expected)


if __name__ == '__main__':
    unittest.main()

