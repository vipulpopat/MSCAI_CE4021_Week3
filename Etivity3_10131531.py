"""
Student number: 10131531
Name: Cathal Cronin
Date: 29/09/2018
"""
from matrix import *

if __name__ == '__main__':

    # Example 2 by 2 Matrices
    matrix_a = Matrix([[2, 4], [1, 8]])
    matrix_b = Matrix([[3, 1], [7, 2]])

    # Example 4 by 4 Matrices
    matrix_c = Matrix([[2, 3, 2, 9], [8, 3, 1, 7], [4, 1, 9, 5], [2, 4, 0, 9]])
    matrix_d = Matrix([[2, 3, 5, 2], [1, 9, 1, 7], [6, 3, 9, 4], [5, 2, 4, 7]])

    # Single column vectors
    vector_e = Matrix([[2], [3], [9]])
    vector_f = Matrix([[1], [9], [5]])
    vector_g = Matrix([[2], [1], [6], [5]])

    # Scalar constant
    scalar = 6

    print('Result: \n%s' % add_matrices(matrix_a, matrix_b))
    print('Result: \n%s' % subtract_matrices(matrix_a, matrix_b))
    print('Result: \n%s' % multiply_matrices(matrix_a, matrix_b))
    print('Result: \n%s' % multiply_matrices(matrix_c, matrix_d))
    print('Result: \n%s' % multiply_matrices(matrix_c, vector_g))
    print('Result: \n%s' % scalar_multiplication(matrix_a, scalar))
    print('Result: \n%s' % dot_product(vector_e, vector_f))
