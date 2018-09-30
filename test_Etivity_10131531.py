"""
Student number: 10131531
Name: Cathal Cronin
Date: 29/09/2018
"""

import unittest

from matrix import *


class TestEtivity3(unittest.TestCase):

    def setUp(self):
        self.matrix_a = Matrix([[2, 4], [1, 8]])
        self.matrix_b = Matrix([[3, 1], [7, 2]])

        self.matrix_c = Matrix([[2, 3, 2, 9], [8, 3, 1, 7], [4, 1, 9, 5], [2, 4, 0, 9]])
        self.matrix_d = Matrix([[2, 3, 5, 2], [1, 9, 1, 7], [6, 3, 9, 4], [5, 2, 4, 7]])

        self.vector_e = Matrix([[2], [3], [9]])
        self.vector_f = Matrix([[1], [9], [5]])
        self.vector_g = Matrix([[2], [1], [6], [5]])

        self.scalar = 6

    def test_add_matrices(self):
        expected_matrix_data = [[5, 5], [8, 10]]
        expected_result = Matrix(expected_matrix_data)

        result = add_matrices(self.matrix_a, self.matrix_b)

        self.assertEqual(result, expected_result)

    def test_subtract_matrices(self):
        expected_matrix_data = [[-1, 3], [-6, 6]]
        expected_result = Matrix(expected_matrix_data)

        result = subtract_matrices(self.matrix_a, self.matrix_b)

        self.assertEqual(result, expected_result)

    def test_multiply_matrices(self):
        expected_matrix_data = [[34, 10], [59, 17]]
        expected_result = Matrix(expected_matrix_data)

        result = multiply_matrices(self.matrix_a, self.matrix_b)

        self.assertEqual(result, expected_result)

    def test_scalar_multiplication_on_matrix(self):
        expected_matrix_data = [[12, 24], [6, 48]]
        expected_result = Matrix(expected_matrix_data)

        result = scalar_multiplication(self.matrix_a, self.scalar)

        self.assertEqual(result, expected_result)

    def test_dot_product_on_vectors(self):
        expected_result = 74
        result = dot_product(self.vector_e, self.vector_f)

        self.assertEqual(result, expected_result)

    def test_4_by_4_matrix_multiplication(self):
        expected_matrix_data = [[64, 57, 67, 96], [60, 68, 80, 90], [88, 58, 122, 86], [53, 60, 50, 95]]
        expected_result = Matrix(expected_matrix_data)

        result = multiply_matrices(self.matrix_c, self.matrix_d)
        self.assertEqual(result, expected_result)

    def test_4_by_4_matrix_by_column_vector_multiplication(self):
        expected_matrix_data = [[64], [60], [88], [53]]
        expected_result = Matrix(expected_matrix_data)

        result = multiply_matrices(self.matrix_c, self.vector_g)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
