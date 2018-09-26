import unittest
from Etivity3_ID18195326 import Matrix

class TestMatrixImplementationEtivity3(unittest.TestCase):
    
    
    """Tests the implementation of the Matrix class for Etivity 3.
    
    Unit tests are:
        1) Create a new matrix and confirm size is correctly reported in a tuple
        2) Add two matrices
        3) Subtract two matrices
        5) Multiply a matrix by a scalar
        6) Multiply a matrix by a vector
        7) Multiply a matrix by a matrix
        8) Test equality and inequality
        
    Edge Cases in this Unit Test are:
        1) Create a new matrix with an empty list or non-list parameter
        2) Perform addition/subtraction of a matrix and a non-matrix
        3) Perform addition/subtraction of a matrix and an incompatible matrix
        4) Multiply a matrix by a non-numeric value
        5) Multiply a matrix by an incompatible matrix
    """
    
    # Internal matrix and (column) vector representations for test cases
    _A_2x2 = [[1,3], [5,7]]
    _B_2x2 = [[2,4], [6,8]]
    
    _B_2x1 = [[2], [1]]
    
    _A_3x3 = [[1,2,3], [0,3,4], [5,6,8]]
    _B_3x3 = [[1,3,6], [2,1,2], [4,2,1]]
    
    _B_3x1 = [[2], [1], [3]]
    
    _B_3x2 = [[4,7], [3,9], [5,2]]
    
        
    def test_matrix_creation(self):
        # Checks that a matrix is created successfully with the correct dimensions and content
        a = Matrix(self._A_2x2)
        self.assertEqual(a.get_order(), (2,2))
        self.assertEqual(a.elements, self._A_2x2)
    
        
    def test_matrix_invalid_creation(self):
        # Checks that a matrix can't be created without a valid element list
        self.assertRaises(ValueError, Matrix, None)
        self.assertRaises(ValueError, Matrix, [])
        
    
        
    def test_matrix_add_matrices(self):
        # Checks that two same size matrices are added together correctly
        a = Matrix(self._A_2x2)
        b = Matrix(self._B_2x2)
        c = a + b
        expected = [[3,7], [11,15]]
        self.assertEqual(c.elements, expected)
    
        
    def test_matrix_add_invalid_matrices(self):
        # Checks that two same differing size matrices can't be added or subtracted
        a = Matrix(self._A_2x2)
        b = Matrix(self._B_3x3)
        
        func = lambda x, y: x + y
        
        self.assertRaises(TypeError, func, a, b)
        self.assertRaises(TypeError, func, a, 3)
        self.assertRaises(TypeError, func, a, "")
               
        
    def test_matrix_subtract_matrices(self):
        # Checks that two same size matrices are added together correctly
        a = Matrix(self._A_2x2)
        b = Matrix(self._B_2x2)
        c = a - b
        expected = [[-1,-1], [-1,-1]]
        self.assertEqual(c.elements, expected)
    
        
    def test_matrix_subtract_invalid_matrices(self):
        # Checks that two same differing size matrices can't be added or subtracted
        a = Matrix(self._A_2x2)
        b = Matrix(self._B_3x3)
        
        func = lambda x, y: x - y
        
        self.assertRaises(TypeError, func, a, b)
        self.assertRaises(TypeError, func, a, 3)
        self.assertRaises(TypeError, func, a, "")


    def test_matrix_multiply_by_scalar(self):
        # Checks the correct multiplication of a matrix by a scalar      
        a = Matrix(self._B_3x2)
        b = a * 3
        expected = [[12,21], [9,27], [15,6]]
        self.assertEqual(b.elements, expected)


    def test_matrix_multiply_by_vector(self):
        # Checks the correct multiplication of a matrix by a vector      
        a = Matrix(self._B_2x2)
        b = Matrix(self._B_2x1)
        c = a * b
        expected = [[8],[20]]
        self.assertEqual(c.elements, expected)

        
    def test_matrix_multiply_same_order_matrices(self):
        # Checks that two same size matrices are multiplied together correctly
        a = Matrix(self._A_2x2)
        b = Matrix(self._B_2x2)
        c = a * b
        expected = [[20,28], [52,76]]
        self.assertEqual(c.elements, expected)
        
        
    def test_matrix_multiply_nonsquare_matrices(self):
        # Checks that two different size matrices are multiplied together correctly
        a = Matrix(self._A_3x3)
        b = Matrix(self._B_3x2)
        c = a * b
        expected = [[25,31], [29,35], [78,105]]
        self.assertEqual(c.elements, expected)
        
        
    def test_matrix_multiply_incompatible_matrices(self):
        # Checks that matrices with incompatible dimension/order can't be multiplied
        a = Matrix(self._A_3x3)
        b = Matrix(self._B_3x2)
        
        func = lambda x, y: x * y
        
        self.assertRaises(TypeError, func, b, a)
        
        
    def test_matrix_multiply_non_numeric(self):
        # Checks that matrices can't be multiplied by a string or non-Matrix object
        a = Matrix(self._A_2x2)
        
        func = lambda x, y: x * y
        
        self.assertRaises(TypeError, func, a, "")
        self.assertRaises(TypeError, func, a, None)
        self.assertRaises(TypeError, func, a, [])
        
    def test_matrix_equality(self):
        # Check that matrix equality rules are correct
        a = Matrix(self._A_2x2)
        b = Matrix(self._B_2x2)        
        c = Matrix([[1,3], [5,7]])
        d = Matrix(self._A_3x3)
        
        self.assertTrue(a != b)
        self.assertTrue(a == c)
        self.assertFalse(a == d)
        self.assertFalse(c == d)
        



        
        
            
