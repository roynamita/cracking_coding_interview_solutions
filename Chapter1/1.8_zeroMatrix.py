"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to O.
"""
import unittest


def solve(matrix):
    """
    Time Complexity : O(m*n(m+n))
    Space Complexity : O(m*n)
    :param matrix:
    :return:
    """
    m = len(matrix)
    n = len(matrix[0])
    new_matrix = [[1 for i in range(n)] for j in range(m)]

    for i in range(m):
        for j in range(n):
            if new_matrix[i][j] == 0:
                continue
            elif matrix[i][j] == 0:
                for k in range(n):
                    new_matrix[i][k] = 0
                for k in range(m):
                    new_matrix[k][j] = 0
            else:
                new_matrix[i][j] = matrix[i][j]
    return new_matrix


def solve_efficient(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows = []
    cols = []

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.append(i)
                cols.append(j)

    for row in rows:
        nullify_row(matrix, row)
    for col in cols:
        nullify_col(matrix, col)
    return matrix


def nullify_row(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0


def nullify_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


class Test(unittest.TestCase):
    data = [[1, 2, 3, 4],
            [5, 6, 0, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]

    expected = [[1, 2, 0, 4],
                [0, 0, 0, 0],
                [9, 10, 0, 12],
                [13, 14, 0, 16]]

    def test_zero_matrix(self):
        actual = solve(self.data)
        self.assertEqual(actual, self.expected)

    def test_zero_matrix_efficient(self):
        actual = solve_efficient(self.data)
        self.assertEqual(actual, self.expected)




if __name__ == '__main__':
    unittest.main()
    data = [[1, 2, 3, 4],
            [5, 6, 0, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]

    print(solve(data))

