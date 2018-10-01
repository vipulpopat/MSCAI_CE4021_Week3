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
        return (rows,columns)

    else:
        raise ValueError('The given matrix is not a valid. Matrix={}'.format(matrix))


def is_matrix(matrix):
    """ Return True if the input paramter is a list."""
    return isinstance(matrix, list)


def matrix_operation(left_matrix, right_matrix, operation):
    """ Perform matrix operations such as: addition, subtraction, multiplication."""

    check_matrix_dimensions_compatible_with_operation(left_matrix, right_matrix, operation)

    #matrix_left_nb_rows, matrix_right_nb_cols = size(left_matrix)    
    #nb_rows, nb_columns = size(right_matrix)    
    #result = create_empty_matrix(nb_columns, matrix_left_nb_rows)
    
    matrix_left_nb_rows, nb_columns = get_dimensions_of_result_matrix(left_matrix, right_matrix)
    result = create_empty_matrix(nb_columns, matrix_left_nb_rows)

    for column in range(nb_columns):
        # for row in range(nb_rows):
        for row in range(matrix_left_nb_rows):
            if (operation == "+"):
                result[row][column] = left_matrix[row][column] + right_matrix[row][column]

            elif(operation == "-"):
                result[row][column] = left_matrix[row][column] - right_matrix[row][column]

            elif(operation == "aidan*"):
                #for k in range(nb_rows):     
                for k in range(nb_columns):     
                    result[row][column] += left_matrix[row][k] * right_matrix[k][column]

            elif(operation == "*"):
                left_matrix_row = get_row_from_matrix(left_matrix, row)
                right_matrix_col = get_column_from_matrix(right_matrix, column)
                result[row][column] =  multiply_row_by_column(left_matrix_row, right_matrix_col)

            else:
                raise ValueError('Unsupported operation:{}'.format(operation))

    return result


def get_dimensions_of_result_matrix(left_matrix, right_matrix):
    matrix_left_nb_rows,  matrix_left_nb_cols  = size(left_matrix)    
    matrix_right_nb_rows, matrix_right_nb_cols = size(right_matrix)    
    return(matrix_left_nb_rows, matrix_right_nb_cols)
    
    
def get_column_from_matrix(matrix, column_index):
    """ Return a single column from a matrix."""
    #return [row[column_index] for row in matrix]
    #return [[row[column_index] for row in matrix]]
    return [[row[column_index]] for row in matrix]


def get_row_from_matrix(matrix, row_index):
    """ Return a single row from a matrix."""
    return [matrix[row_index]]


def multiply_row_by_column(row_matrix, column_matrix):
    """ Multiply a row with a column.  """

    row_matrix_nb_rows, row_matrix_nb_columns = size(row_matrix)
    col_matrix_nb_rows, col_matrix_nb_columns = size(column_matrix)
    if (row_matrix_nb_columns != col_matrix_nb_rows):
        raise ValueError('Matrix sizes not compatible. row_matrix_nb_columns={} col_matrix_nb_rows={}'.format(row_matrix_nb_columns, col_matrix_nb_rows))

    result = 0;

    for index in range(row_matrix_nb_columns):
        result +=row_matrix[0][index] * column_matrix[index][0]

    return result


def check_matrix_dimensions_compatible_with_operation(left_matrix, right_matrix, operation):
    """ Throw an exception if the 2 matrices cannot be added/substracted/multiplied """
    
    nb_row_left_matrix, nb_col_left_matrix = size(left_matrix)
    nb_row_right_matrix, nb_col_right_matrix = size(right_matrix)
    
    if (operation == "*" and nb_col_left_matrix != nb_row_right_matrix):
        raise ValueError("Matrices not suited for multiplications")
        
    elif ((operation == "+" or operation == "-") and 
          (nb_row_left_matrix != nb_row_right_matrix or nb_col_left_matrix != nb_col_right_matrix)):
        raise ValueError("Matrices not suited for addition/substraction")


def check_matrix_dimensions_compatible_with_multiplication(left_matrix, right_matrix):
    """ Throw an exception if the 2 matrices cannot be multiplied """
    nb_row_left_matrix, nb_col_left_matrix = size(left_matrix)
    nb_row_right_matrix, nb_col_right_matrix = size(right_matrix)
    
    if (nb_col_left_matrix != nb_row_right_matrix):
        raise ValueError('Matrix size mismatch error: left_matrix.nb_col={} right_matrix.nb_row={}'.format(nb_col_left_matrix, nb_row_right_matrix))


def create_empty_matrix(nb_columns, nb_rows):
    """ Initialise an empty matrix."""
    new_matrix = [[0 for x in range(nb_columns)] for y in range(nb_rows)]
    return new_matrix


#
# Only test related functions below this point.
#
def print_header(test_name):
    print("="*20 + " " + test_name + " " + "="*20)


def test_matrix_size(test_name, matrix, expected_size):
    print_header(test_name)
    result = size(matrix)
    print("Matrix: {0}".format(matrix))
    print("Size  : {0}".format(result))
    assert( expected_size == result)


def test_square_matrix_operations(test_name, matrix_a, matrix_b, expected_a_plus_b, expected_a_minus_b,
                                   expected_a_times_b):
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

    matrix = [[1,2],[3,4]]
    test_matrix_size("test  size calculation of matrix 3x1", matrix, (2, 2))

    matrix = [[11,12,13]]
    test_matrix_size("test  size calculation of matrix 3x1", matrix, (1, 3))

    matrix = [[11,12,13],[21,22,23]]
    test_matrix_size("test  size calculation of matrix 3x2", matrix, (2, 3))


    # rainy day tests
    exception_caught = False
    try:
        matrix = 11
        test_matrix_size("test size calculation of matrix 1x1", matrix, (1,1))
    except ValueError as e:
        print ("{0}".format(e))
        exception_caught = True
    assert exception_caught == True


def run_test_square_matrix_operations():
    # Test 2x2 matrix operations
    matrix_a = [[1,2],[3,4]]
    matrix_b = [[5,6],[7,8]]
    
    expected_a_plus_b = [[6, 8], [10, 12]]
    expected_a_minus_b = [[-4, -4], [-4, -4]]
    expected_a_times_b = [[19, 22], [43, 50]]

    test_square_matrix_operations("test 2x2 matrix operations", 
                                   matrix_a, matrix_b,
                                   expected_a_plus_b, expected_a_minus_b,
                                   expected_a_times_b)

    # Test 4x4 matrix operations
    matrix_a = [[9,8,7,6],[5,4,3,2],[1,0,9,8],[7,6,5,4]]
    matrix_b = [[1,2,3,4],[5,6,7,8],[9,0,1,2],[3,4,5,6]]

    expected_a_plus_b = [[10, 10, 10, 10], [10, 10, 10, 10], [10, 0, 10, 10], [10, 10, 10, 10]]
    expected_a_minus_b = [[8, 6, 4, 2], [0, -2, -4, -6], [-8, 0, 8, 6], [4, 2, 0, -2]]
    expected_a_times_b = [[130, 90, 120, 150], [58, 42, 56, 70], [106, 34, 52, 70], [94, 66, 88, 110]]

    test_square_matrix_operations("test 4x4 matrix operations", 
                                   matrix_a, matrix_b,
                                   expected_a_plus_b, expected_a_minus_b,
                                   expected_a_times_b)

    
def run_test_matrix_by_vector_multiplications():

    matrix_a = [[9,8,7,6],[5,4,3,2],[1,0,9,8],[7,6,5,4]]
    matrix_b = [[1],[2],[3],[4]]

    expected_a_times_b = [[70], [30], [60], [50]]
    
    test_matrix_by_matrix_multiplications("test matrix by vector multiplication", matrix_a, matrix_b, expected_a_times_b)


def run_test_matrix_by_matrix_multiplications():
    
    matrix_a = [[9,8,7,6],[5,4,3,2],[1,0,9,8],[7,6,5,4]]
    matrix_b = [[1,5],[2,6],[3,7],[4,8]]

    expected_a_times_b = [[70,190], [30,86], [60,132], [50,138]]

    test_matrix_by_matrix_multiplications("test 4x4 matrix by 4x2 matrix multiplication", matrix_a, matrix_b, expected_a_times_b)

    matrix_a = [[9,8,7,6],[5,4,3,2]]
    matrix_b = [[1,5],[2,6],[3,7],[4,8]]

    expected_a_times_b = [[70, 190], [30, 86]]

    test_matrix_by_matrix_multiplications("test 2x4 matrix by 4x2 matrix multiplication", matrix_a, matrix_b, expected_a_times_b)


#
# Run the test suite
#
run_test_matrix_size()
run_test_square_matrix_operations()
run_test_matrix_by_vector_multiplications()
run_test_matrix_by_matrix_multiplications()