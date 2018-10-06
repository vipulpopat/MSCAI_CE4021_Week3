
def check_size(Inputdata):
    rows = len(Inputdata)
    columns = len(Inputdata[0])
    return (rows , columns)

def check_size_for_multiplication(first_matrix,second_matrix):
    if (len(first_matrix[0]) == len(second_matrix)):
        return True
    else:
        return False

def addORsub(Matrix_A,Matrix_B, operation):
    if check_size(Matrix_A) == check_size(Matrix_B):
        check = check_size(Matrix_A)
        countrow = check[0]
        countcolumn = check[1]
        rowlist=[]
        operations = ['+','-']
        if operation in operations:
             if (countrow == 2 and countcolumn == 2):
                for x in range(countrow):
                    collist=[]
                    for y in range(countcolumn):
                        if operation == '+':
                            Matrix_Add = Matrix_A[x][y] + Matrix_B[x][y]
                            collist.append(Matrix_Add)
                        elif operation == '-':
                            Matrix_Sub = Matrix_A[x][y] - Matrix_B[x][y]
                            collist.append(Matrix_Sub)
                    rowlist.append(collist)
                return rowlist

def multiplication(Matrix_A,Matrix_B):
    Matrix_Mul = [[sum(a*b for a,b in zip(Matrix_A_row,Matrix_B_col)) for Matrix_B_col in zip(*Matrix_B)] for Matrix_A_row in Matrix_A]
    return Matrix_Mul


MatrixA = [[5, 6], [7, 8]]
MatrixB = [[9, 10], [11, 12]]

print("Input:", MatrixA, '\n')
print("Input:", MatrixB, '\n')

MatrixAdd = addORsub(MatrixA , MatrixB, '+')

print("Addition of 2*2 Matrix")
print(MatrixAdd, '\n')

MatrixSub = addORsub(MatrixA , MatrixB, '-')

print("Subtraction of 2*2 Matrix")
print(MatrixSub, '\n')


MatrixMultiply = multiplication(MatrixA , MatrixB)
print("Multiplication of Matrix")
print(MatrixMultiply, '\n')

