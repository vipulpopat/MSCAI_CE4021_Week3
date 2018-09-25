def matrix_get_size(matrix):
    """
    Matrix size is (number of rows, number of columns)
    """
    return (len(matrix), len(matrix(0)))

#Test 1 - test a function to return the size of a 2x2 matrix.
two_by_two_matrix = ((2,3),(5,1))
print (matrix_get_size(two_by_two_matrix))