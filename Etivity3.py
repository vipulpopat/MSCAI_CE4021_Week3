"""
Aim:
1) Providing the size of a matrix as a 2-dimensional tuple
2) Summing and subtracting two matrices
3) Multiplying two matrices or a vector and a matrix of suitable size
"""

def size(matrix):
    """
    Return the size of a 2D matrix.
    """

    if is_matrix(matrix):
        columns = len(matrix[0])
        rows = len(matrix)
        return (rows, columns)

    else:
        raise ValueError('The given matrix is not a valid. Matrix={}'.format(matrix))


def is_matrix(matrix):
    """ Return True if the input paramter is a list."""
    return isinstance(matrix, list) and isinstance(matrix[0], list)


def matrix_operation(matrix_a, matrix_b, operation):
    """ Perform matrix operations such as: addition, subtraction, multiplication."""

    check_matrix_dimensions_compatible_with_operation(matrix_a, matrix_b, operation)

    nb_rows, nb_columns = get_dimensions_of_result_matrix(matrix_a, matrix_b)
    result = create_empty_matrix(nb_rows, nb_columns)

    for col in range(nb_columns):
        for row in range(nb_rows):
            if operation == "+":
                result[row][col] = matrix_a[row][col] + matrix_b[row][col]

            elif operation == "-":
                result[row][col] = matrix_a[row][col] - matrix_b[row][col]

            elif operation == "*":
                matrix_a_row = get_row_from_matrix(matrix_a, row)
                matrix_b_col = get_col_from_matrix(matrix_b, col)
                result[row][col] = multiply_row_by_column(matrix_a_row, matrix_b_col)

            else:
                raise ValueError('Unsupported operation:{}'.format(operation))

    return result


def get_dimensions_of_result_matrix(matrix_a, matrix_b):
    """ Return a tuple describing the size of the result matrix. """
    matrix_a_nb_rows, matrix_a_nb_cols = size(matrix_a)
    matrix_b_nb_rows, matrix_b_nb_cols = size(matrix_b)
    return(matrix_a_nb_rows, matrix_b_nb_cols)


def get_row_from_matrix(matrix, row_index):
    """ Return a single row from a matrix."""
    return [matrix[row_index]]


def get_col_from_matrix(matrix, column_index):
    """ Return a single column from a matrix."""
    return [[row[column_index]] for row in matrix]


def multiply_row_by_column(row_matrix, column_matrix):
    """ Multiply a row with a column.  """

    row_matrix_nb_rows, row_matrix_nb_columns = size(row_matrix)
    col_matrix_nb_rows, col_matrix_nb_columns = size(column_matrix)
    if row_matrix_nb_columns != col_matrix_nb_rows:
        raise ValueError("Can't multiply row:{} by column:{}"
                         .format(row_matrix, column_matrix))

    result = 0;

    for index in range(row_matrix_nb_columns):
        result += row_matrix[0][index] * column_matrix[index][0]

    return result


def check_matrix_dimensions_compatible_with_operation(matrix_a, matrix_b, operation):
    """ Throw an exception if the 2 matrices cannot be added/substracted/multiplied """

    nb_row_matrix_a, nb_col_matrix_a = size(matrix_a)
    nb_row_matrix_b, nb_col_matrix_b = size(matrix_b)

    if (operation == "*" and nb_col_matrix_a != nb_row_matrix_b):
        raise ValueError("Matrices not suited for multiplications")

    elif ((operation == "+" or operation == "-") and
          (nb_row_matrix_a != nb_row_matrix_b or nb_col_matrix_a != nb_col_matrix_b)):
        raise ValueError("Matrices not suited for addition/substraction")


def create_empty_matrix(nb_rows, nb_columns):
    """ Initialise an empty matrix."""
    new_matrix = [[0 for x in range(nb_columns)] for y in range(nb_rows)]
    return new_matrix


#
# Only test related functions below this point.
#
def print_header(test_name):
    """ Print a test header. """
    print("="*20 + " " + test_name + " " + "="*20)


def test_matrix_size(test_name, matrix, expected_size):
    """ Generic test case for testing size. """
    print_header(test_name)
    result = size(matrix)
    print("Matrix: {0}".format(matrix))
    print("Size  : {0}".format(result))
    assert expected_size == result


def test_square_matrix_operations(test_name, matrix_a, matrix_b, expected_a_plus_b, expected_a_minus_b,
                                   expected_a_times_b):
    """ Generic test case for matrix operations. """
    print_header(test_name)
    a_plus_b = matrix_operation(matrix_a, matrix_b, "+")
    a_minus_b = matrix_operation(matrix_a, matrix_b, "-")
    a_times_b = matrix_operation(matrix_a, matrix_b, "*")

    print("Matrix A     :{}".format(matrix_a))
    print("Matrix B     :{}".format(matrix_b))
    print("Matrix A + B :{}".format(a_plus_b))
    print("Matrix A - B :{}".format(a_minus_b))
    print("Matrix A * B :{}".format(a_times_b))

    assert a_plus_b == expected_a_plus_b
    assert a_minus_b == expected_a_minus_b
    assert a_times_b == expected_a_times_b


def test_matrix_by_matrix_multiplications(test_name, matrix_a, matrix_b, expected_a_times_b):
    """ Generic test case for matrix multiplications. """
    
    print_header(test_name)

    a_times_b = matrix_operation(matrix_a, matrix_b, "*")
    print("Matrix A     :{}".format(matrix_a))
    print("Matrix B     :{}".format(matrix_b))
    print("Matrix A * B :{}".format(a_times_b))

    assert a_times_b == expected_a_times_b


#
# Run the above test code with real matrices.
#
def run_test_matrix_size():
    """ Performs matrix size test using real data. """

    matrix = [[1, 2], [3, 4]]
    test_matrix_size("test  size calculation of matrix 3x1", matrix, (2, 2))

    matrix = [[11, 12, 13]]
    test_matrix_size("test  size calculation of matrix 3x1", matrix, (1, 3))

    matrix = [[11, 12, 13], [21, 22, 23]]
    test_matrix_size("test  size calculation of matrix 3x2", matrix, (2, 3))


    # rainy day tests
    exception_caught = False
    try:
        matrix = 11
        test_matrix_size("test size calculation of matrix 1x1", matrix, (1, 1))
    except ValueError as exception:
        print("{0}".format(exception))
        exception_caught = True
    assert exception_caught


def run_test_square_matrix_operations():
    """ Performs matrix operation using real data."""
    # Test 2x2 matrix operations
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]

    expected_a_plus_b = [[6, 8], [10, 12]]
    expected_a_minus_b = [[-4, -4], [-4, -4]]
    expected_a_times_b = [[19, 22], [43, 50]]

    test_square_matrix_operations("test 2x2 matrix operations",
                                   matrix_a, matrix_b,
                                   expected_a_plus_b, expected_a_minus_b,
                                   expected_a_times_b)

    # Test 4x4 matrix operations
    matrix_a = [[9, 8, 7, 6], [5, 4, 3, 2], [1, 0, 9, 8], [7, 6, 5, 4]]
    matrix_b = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2], [3, 4, 5, 6]]

    expected_a_plus_b = [[10, 10, 10, 10], [10, 10, 10, 10], [10, 0, 10, 10], [10, 10, 10, 10]]
    expected_a_minus_b = [[8, 6, 4, 2], [0, -2, -4, -6], [-8, 0, 8, 6], [4, 2, 0, -2]]
    expected_a_times_b = [[130, 90, 120, 150], [58, 42, 56, 70], [106, 34, 52, 70], [94, 66, 88, 110]]

    test_square_matrix_operations("test 4x4 matrix operations",
                                   matrix_a, matrix_b,
                                   expected_a_plus_b, expected_a_minus_b,
                                   expected_a_times_b)


def run_test_matrix_by_vector_multiplications():
    """ Performs matrix by vector multiplications using real data."""

    matrix_a = [[9, 8, 7, 6], [5, 4, 3, 2], [1, 0, 9, 8], [7, 6, 5, 4]]
    matrix_b = [[1], [2], [3], [4]]

    expected_a_times_b = [[70], [30], [60], [50]]

    test_matrix_by_matrix_multiplications("test matrix by vector multiplication", matrix_a, matrix_b, expected_a_times_b)


def run_test_matrix_by_matrix_multiplications():
    """ Performs matrix by matrix multiplications using real data."""

    matrix_a = [[9, 8, 7, 6], [5, 4, 3, 2], [1, 0, 9, 8], [7, 6, 5, 4]]
    matrix_b = [[1, 5], [2, 6], [3, 7], [4, 8]]

    expected_a_times_b = [[70, 190], [30, 86], [60, 132], [50, 138]]

    test_matrix_by_matrix_multiplications("test 4x4 matrix by 4x2 matrix multiplication", matrix_a, matrix_b, expected_a_times_b)

    matrix_a = [[9, 8, 7, 6], [5, 4, 3, 2]]
    matrix_b = [[1, 5], [2, 6], [3, 7], [4, 8]]

    expected_a_times_b = [[70, 190], [30, 86]]

    test_matrix_by_matrix_multiplications("test 2x4 matrix by 4x2 matrix multiplication", matrix_a, matrix_b, expected_a_times_b)


#
# Run the test suite
#
run_test_matrix_size()
run_test_square_matrix_operations()
run_test_matrix_by_vector_multiplications()
run_test_matrix_by_matrix_multiplications()
