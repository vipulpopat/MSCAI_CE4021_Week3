# Student Name:    Mark Murnane
# Student ID:      18195326

from numbers import Number

# Write Python functions for the following operations on matrices without making use of imported modules:
#    Providing the size of a matrix as a 2-dimensional tuple
#    Summing and subtracting two matrices
#    Multiplying two matrices or a vector and a matrix of suitable size


class Matrix(object):
    
    """This class represents a mathematical Matrix for use in Linear Algebra
    
    A matrix is a rectangular structure of m x n elements, where m is the number of columns in the matrix and n is the number of rows.
    N.B. All rows of the matrix must be of equal size.
    
    """
    
    _ROWS = 0
    _COLS = 1
    
    def __init__ (self, element_data):
        """Creates a new instance of a Matrix.
        
        Args:
            element_data[[row_data]+]    A list containing other 1 or more lists representing each row of the matrix.
            
        Return:
            Matrix  Instance of the Matrix class, or None if the element_data is not valid.
        """
        self.order = (len(element_data), len(element_data[0]))
        self.elements = element_data
        
        
    def get_order(self):
        """Returns a tuple with the order of the matrix, i.e. (rows x columns)."""
        return self.order
        
        
    def get_size(self):
        """Returns a tuple with the order of the matrix, i.e. (rows x columns)."""
        return self.order
    
    
    def __str__(self):
        mat_str = ''
        for row in self.elements:           
            row_str = ''
            for col_val in row:
                row_str = row_str + ' ' + str(col_val) + ' '            
            mat_str = mat_str + row_str + '\n'
    
        return mat_str
    


    def _is_valid_add_sub_eq_matrix(self, other):
        """Internal helper function that checks if this matrix and other are valid for equality, addition or subtraction.
        
        To be valid for these operations both must be matrices with the same order.
        """
          
        if not isinstance(other, self.__class__):
            return False
        
        if self.get_order() != other.get_order():
            return False
        
        return True
    
    def _is_valid_matrix_multiplier(self, other):
        """Internal helper function that checks if this matrix and other can be validly multiplied.  
        
        To be valid the number of columns in this matrix must equal the number of rows in other.
        """
        
        if not isinstance(other, self.__class__):
            return False
        
        if self.order[Matrix._COLS] != other.order[Matrix._ROWS]:
            return False

        return True
    
    
    def __eq__(self, other):
        """Compares this matrix object to another matrix object.  Returns true if the order of the matrix is the same and the elements at each position are the same."""
        
        if self._is_valid_add_sub_eq_matrix(other):
            for self_row, other_row in zip(self.elements, other.elements):
                if self_row != other_row:
                    return False
            return True           
        else:
            return False
    
    

    def _apply_function_to_elements(self, other, lfunc):
        return [list(map(lfunc, self_row, other_row)) for self_row, other_row in zip(self.elements, other.elements) ]
        
        
    def __add__(self, other):
        if self._is_valid_add_sub_eq_matrix(other):
            return Matrix (self._apply_function_to_elements(other, lambda x, y: x + y))
        else:
            return None        
    
        
    def __sub__(self, other):        
        if self._is_valid_add_sub_eq_matrix(other):
            return Matrix (self._apply_function_to_elements(other, lambda x, y: x - y))
        else:
            return None        
    
            
    def __mul__(self, other):

        """Multiplies this matrix by a scalar value or another matrix."""
        new_matrix = None
        
        if isinstance(other, Number):
            # Scalar multiplication uses list comprehension with a map to multiply each element by the scalar
            new_elements = [list(map(lambda element: element*other, row)) for row in self.elements]
            new_matrix = Matrix(new_elements)
        elif self._is_valid_matrix_multiplier(other):
            # Matrix multiplication C=AB, i.e. c = (self)(other)
            c_order = (self.order[Matrix.__COLS], other.order[Matrix._COLS])

            # Initialise the elements array to an m*n array of 0s
            c = [[0]*c_order[Matrix._COLS] for i in range(c_order[Matrix._ROWS])]
            
            # For each position in the new matrix c, calculate the values from this matrix and other
            for i in range(c_order[Matrix._ROWS]):
                for k in range(c_order[Matrix._COLS]):
                    for j in range(self.order[Matrix._COLS]):
                        c[i][k] += (self.elements[i][j] * other.elements[j][k])              
                                    
            new_matrix = c
            
        return new_matrix
            
                      
            
a = Matrix([[1, 2, 3], [0, 3, 4], [5, 6, 8]])
print(a)

b = a*8
print(b)

c = Matrix([[1, 2, 3], [0, 3, 4], [5, 6, 8]])

print(a == b)
print(a == c)
  

d = a + c
print(d)

e = b - a
print(e)


print ("Matrix multiplication")

f = Matrix([[1, 1], [2, 2]])
g = Matrix([[2], [1], [3]])
h = Matrix([[1, 2, 3]])
i = Matrix([[2, 1], [1, 2], [3, 0]])

print(f)
print(g)
print(h)
print(i)


print(a._is_valid_matrix_multiplier(b))
print(a._is_valid_matrix_multiplier(f))
print(a._is_valid_matrix_multiplier(g))
print(a._is_valid_matrix_multiplier(h))
print(a._is_valid_matrix_multiplier(i))

print(a * g)