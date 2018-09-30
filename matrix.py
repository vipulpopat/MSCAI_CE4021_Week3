"""
Student number: 10131531
Name: Cathal Cronin
Date: 25/09/2018
"""


class Matrix:

    def __init__(self, matrix_data=[]):
        """Matrix class to represent an M X N matrix, filled with the data provided.

        Args:
            matrix_data: A list of lists containing the data of the matrix, by default set to empty.
            fill_matrix: An optional flag to set which will auto-fill the matrix with random values.
                Setting this to true will override the data argument.
        """
        if matrix_data:

            rows = len(matrix_data)

            if isinstance(matrix_data[0], list):
                cols = len(matrix_data[0])
            else:
                cols = 1

            if rows > 0 and cols > 0:
                self.rows = rows
                self.cols = cols
                self.matrix = matrix_data
            else:
                print('Bad matrix data rows and col lists must be > 0')

        else:
            print('Matrix data not set, creating empty matrix')
            self.rows = 0
            self.cols = 0
            self.matrix = []

    def __str__(self):
        """Return a string representation of matrix."""
        matrix_str_format = []
        for row in self.matrix:
            for col_val in row:
                matrix_str_format.append(str(col_val) + ' ')

            matrix_str_format.append('\n')

        matrix_as_string = ''.join(matrix_str_format)

        return matrix_as_string

    def __eq__(self, other):
        """Return true or false if one matrix is equal to another"""

        for m1_row, m2_row in zip(self.matrix, other.matrix):
            for m1_val, m2_val in zip(m1_row, m2_row):
                if m1_val != m2_val:
                    return False

        return True

    def is_equal(self, other_matrix):
        """Compare one matrix to another to see if they are equal in dimension NOT Contents

        Args:
            other_matrix: Matrix Object

        Returns:
            Boolean value if matrices have the same dimensions.
        """
        other_matrix_rows, other_matrix_cols = other_matrix.rows, other_matrix.cols

        if self.rows == other_matrix_rows and self.cols == other_matrix_cols:
            return True
        else:
            return False

    # def generate_matrix(self, rows_length, cols_length):
    #     """Generate a matrix with dimensions rows X cols.
    #
    #     Args:
    #         matrix_size (tuple) 2-tuple of row and col size.
    #
    #     Returns:
    #         Return a matrix of row X cols, filled with random numbers.
    #     """
    #     # List comprehension to create an rows X cols matrix filled with random values between min and max
    #     print("Creating Matrix")
    #     matrix = [[random.randint(1, 10) for j in range(cols_length)] for i in range(rows_length)]
    #     print(matrix)
    #
    #     return matrix


def perform_matrices_operation(matrix_a, matrix_b, operation):
    """Perform the given operation on 2 matrices.

    Args:
        matrix_a: Matrix object
        matrix_b: Matrix object
        operation: str with value `+` or `-`

    Returns:
        A new matrix from the result of performing the operation on matrix a and matrix b
    """
    if matrix_a.is_equal(matrix_b):
        temp_matrix_data = []
        for m1, m2 in zip(matrix_a.matrix, matrix_b.matrix):

            temp_row_data = []
            for m1_num, m2_num in zip(m1, m2):
                sum_value = eval(str(m1_num) + operation + str(m2_num))
                temp_row_data.append(sum_value)

            temp_matrix_data.append(temp_row_data)

        return Matrix(temp_matrix_data)

    else:
        print('Error Matrices not same dimensions')


def add_matrices(matrix_a, matrix_b):
    """Add 2 matrices together"""
    print("Adding Matrix A and Matrix B")
    return perform_matrices_operation(matrix_a, matrix_b, operation='+')


def subtract_matrices(matrix_a, matrix_b):
    """Subtract 2 matrices from each other"""
    print("Subtracting Matrix A and Matrix B")
    return perform_matrices_operation(matrix_a, matrix_b, operation='-')


def scalar_multiplication(matrix_a, scalar_b):
    """Multiply a scalar value by a matrix"""
    print("Performing scalar multiplication on matrix.")
    print("Scalar Value: %s" % scalar_b)
    temp_data = []
    for m1_row in matrix_a.matrix:
        temp_data.append([num * scalar_b for num in m1_row])

    scalar_matrix = Matrix(temp_data)

    return scalar_matrix


def dot_product(vector_a, vector_b, scalar_multiplication=False):
    """Perform dot product give 2 vectors.

    Args:
        vector_a: Matrix object to represent a row or column vector
        vector_b: Matrix object to represent a row or column vector
        scalar_multiplication: Flag to indicate how to sum elements.

    Returns:
        The dot product sum of the two vectors.
    """

    if vector_a.rows == vector_b.rows:
        dot_product_sum = 0
        for v1_num, v2_num in zip(vector_a.matrix, vector_b.matrix):

            if scalar_multiplication:
                dot_product_sum += v1_num * v2_num
            else:
                dot_product_sum += v1_num[0] * v2_num[0]

        return dot_product_sum

    else:
        print('Error: Matrices cannot be multiplied')
        return -1


def multiply_matrices(matrix_a, matrix_b):
    """multiply matrix a by matrix b

    Args:
        matrix_a: Matrix object
        matrix_b: Matrix object

    Returns:
        A new Matrix object from the resulting multiplication

    """
    print("Multiplying matrices")
    print(matrix_a)
    print(matrix_b)

    temp_new_matrix = []
    if matrix_a.cols == matrix_b.rows:

        for i, row in enumerate(matrix_a.matrix):

            new_matrix_row = []
            row_vector = Matrix(row)

            for j in range(matrix_b.cols):
                col_vector = get_matrix_column(matrix_b, j)

                # Multiplication of matrices can be seen as the repeated dot_product. Good way to reuse a method.
                sum = dot_product(row_vector, col_vector, scalar_multiplication=True)
                new_matrix_row.append(sum)

            temp_new_matrix.append(new_matrix_row)

        product_matrix = Matrix(temp_new_matrix)

        return product_matrix
    else:
        print('Matrices cannot be multiplied')
        return -1


def get_matrix_column(matrix, index):
    """Given a matrix and an column index, return the column values of that matrix as a vector object.

    Args:
        matrix: Matrix object
        index: Index of column to return as a vector
    """
    column_vector = []

    for row in matrix.matrix:
        column_vector.append(row[index])

    return Matrix(column_vector)
