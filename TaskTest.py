# Student Name:    Mark Murnane
# Student ID:      18195326

from Etivity3_ID18195326_Matrix import Matrix


### 
### Calculations to test Matrix implementation vs handwritten worked samples
###

# Construct the matrices
a = Matrix([[1,3], [5,7]])
b = Matrix([[2,4], [6,8]])
v = Matrix([[2], [1]])

print("Matrices")

print("A = ")
print(a)

print("B = ")
print(b)

print("V = ")
print(v)

###
### Size
###
print(f"Size of A is {a.get_order()}")

###
### Multiplication
###
c = a @ b
print ("A @ B = ")
print (c)

###
### Addition
###
c = a + b
print ("A + B = ")
print (c)


###
### Subtraction
###
c = a - b
print ("A - B = ")
print (c)

###
### Vector
###
c = b @ v
print ("B @ V = ")
print (c)
