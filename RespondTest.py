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

print("C = ")
print(c)

print("V = ")
print(v)

###
### Size
###
print(f"Size of A is {a.get_order()}")
print(f"Size of B is {b.get_order()}")
print(f"Size of C is {c.get_order()}")
print(f"Size of V is {v.get_order()}")
print("\n\n")

###
### Multiplication
###
h = a @ b
print ("A . B = ")
print (h)

h = a @ c
print ("A . C = ")
print (h)

h = b * 3
print("B x 3 = ")
print (h)

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

###
### Vector
###
h = b @ v
print ("B . V = ")
print (h)

# h = v * b
# print ("V * B = ")
# print (h)

h =  2 * a
print("2 x A = ")
print (h)

h = a * 2
print("A x 2 = ")
print(h)