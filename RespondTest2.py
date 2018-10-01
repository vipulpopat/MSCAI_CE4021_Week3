# Student Name:    Mark Murnane
# Student ID:      18195326

from Etivity3_ID18195326_Matrix import Matrix


### 
### Calculations to test Matrix implementation vs handwritten worked samples
###

# Construct the matrices
a = Matrix([[1,2,4,6], [3,0,2,8], [5,7,1,9], [2,1,8,6]])
b = Matrix([[5,2,1,6], [4,8,7,9], [6,0,3,8], [1,5,4,2]])
c = Matrix([[1,6], [2,8], [3,9], [7,4]])
v = Matrix([[5], [2], [0], [1]])

print("Matrices")

print("A = ")
print(a)

print("B = ")
print(b)

print("V = ")
print(v)


###
### Addition
###
h = a + b
print ("A + B = ")
print (h)


###
### Subtraction
###
h = a - b
print ("A - B = ")
print (h)


h = a @ b
print ("A * B = ")
print (h)


###
### Vector
###
h = a @ v
print ("A * V = ")
print (h)
