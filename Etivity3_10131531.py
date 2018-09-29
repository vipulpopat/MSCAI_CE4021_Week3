"""
Student number: 10131531
Name: Cathal Cronin
Date: 25/09/2018
"""
import random


class Matrix:

    def __init__(self, matrix_size, fill_matrix=True):

        rows, cols = matrix_size
        if rows > 0 and cols > 0:
            self.rows = rows
            self.cols = cols

            if fill_matrix:
                self.matrix = self.generate_matrix(self.rows, self.cols)
            else:
                self.matrix = []
        else:
            print('Error: Given negative values for matrix dimensions')
            return

    def is_equal(self, other):
        """Compare one matrix to another to see if they are equal in dimension NOT Contents

        Args:
            other:

        Returns:

        """
        other_matrix_rows, other_matrix_cols = other.rows, other.cols

        if self.rows == other_matrix_rows and self.cols == other_matrix_cols:
            return True
        else:
            return False

    def set_matrix(self, new_matrix):
        self.matrix = new_matrix

    def generate_matrix(self, rows_length, cols_length):
        """Generate a matrix with dimensions rows X cols.

        Args:
            matrix_size (tuple) 2-tuple of row and col size.

        Returns:
            Return a matrix of row X cols, filled with random numbers.
        """
        # List comprehension to create an rows X cols matrix filled with random values between min and max
        print("Creating Matrix")
        matrix = [[random.randint(1, 10) for j in range(cols_length)] for i in range(rows_length)]
        print(matrix)

        return matrix


def add_matrices(matrix_a, matrix_b):
    print("Adding Matrix A and Matrix B")
    perform_matrices_operation(matrix_a, matrix_b, operation='+')


def subtract_matrices(matrix_a, matrix_b):
    print("Subtracting Matrix A and Matrix B")
    perform_matrices_operation(matrix_a, matrix_b, operation='-')


def scalar_multiplication(matrix_a, scalar_b):
    print("Performing scalar multiplication on matrix")
    scalar_matrix = []
    for m1_row in matrix_a.matrix:
        scalar_matrix.append([num * scalar_b for num in m1_row])

    print(scalar_matrix)


def dot_product(vector_a, vector_b, scalar_multiplication=False):
    print("Dot Product of: %s %s" % (vector_a, vector_b))

    if vector_a.rows == vector_b.rows:
        dot_product_sum = 0
        for v1_num, v2_num in zip(vector_a.matrix, vector_b.matrix):

            if scalar_multiplication:
                dot_product_sum += v1_num * v2_num
            else:
                dot_product_sum += v1_num[0] * v2_num[0]

        print("Dot product sum: %s" % dot_product_sum)
        return dot_product_sum

    else:
        print()


def multiply_matrixes(matrix_a, matrix_b):
    print("Multiplying matrices...")
    display_matrix(matrix_a)
    display_matrix(matrix_b)

    new_matrix = []
    if matrix_a.cols == matrix_b.rows:

        for i, row in enumerate(matrix_a.matrix):
            new_row = Matrix((1, matrix_b.cols), fill_matrix=False)
            new_row.set_matrix(row)
            new_matrix_row = []

            for j in range(matrix_a.cols):
                col_vector = get_matrix_column(matrix_b, i)
                sum = dot_product(new_row, col_vector, scalar_multiplication=True)
                new_matrix_row.append(sum)

            new_matrix.append(new_matrix_row)

        print(new_matrix)


def get_matrix_column(matrix, index):
    col_matrix = Matrix((1, matrix.cols), fill_matrix=False)
    column_vector = []

    for row in matrix.matrix:
        column_vector.append(row[index])

    col_matrix.set_matrix(column_vector)

    return col_matrix

def perform_matrices_operation(matrix_a, matrix_b, operation):
    if matrix_a.is_equal(matrix_b):

        new_matrix_size = (matrix_a.rows, matrix_a.cols)
        new_matrix = Matrix(new_matrix_size, fill_matrix=False)

        for m1, m2 in zip(matrix_a.matrix, matrix_b.matrix):
            print(m1, m2)

            sum_part = []
            for m1_num, m2_num in zip(m1, m2):
                sum_part.append(eval(str(m1_num) + operation + str(m2_num)))

            new_matrix.matrix.append(sum_part)

        display_matrix(new_matrix)
    else:
        print('Error Matrices not same dimensions')


def display_matrix(matrix):
    print("Result...")
    for row in matrix.matrix:
        print(row)
    print()


if __name__ == '__main__':
    matrix_a_size = (2, 2)
    matrix_b_size = (2, 2)
    matrix_c_size = (-1, 3)

    vector_d_size = (3, 1)
    vector_e_size = (3, 1)

    matrix_a = Matrix(matrix_a_size)
    matrix_b = Matrix(matrix_b_size)
    matrix_c = Matrix(matrix_c_size)
    vector_d = Matrix(vector_d_size)
    vector_e = Matrix(vector_e_size)
    scalar = 6

    add_matrices(matrix_a, matrix_b)
    subtract_matrices(matrix_a, matrix_b)
    scalar_multiplication(matrix_a, scalar)
    dot_product(vector_d, vector_e)
    multiply_matrixes(matrix_a, matrix_b)
