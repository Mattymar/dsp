from sympy.matrices import Matrix, Transpose
import math

A = Matrix([[1, 2, 3], [2, 7, 4]])
B = Matrix([[1, -1], [0, 1]])
C = Matrix([[5, -1], [9, 1], [6, 0]])
D = Matrix([[3, -2, -1], [1, 2, 3]])
u = Matrix([[6, 2, -3, 5]])
v = Matrix([[3, 5, -1, 4]])
w = Matrix([[1], [8], [0], [5]])

# Problem 1: Matrix Dimensions
probs = [('1.1', A), ('1.2', B), ('1.3', C), ('1.4', D), ('1.5', u), ('1.6', w)]

for prob in probs:
    print(prob[0] + ': ' + str(prob[1].shape))

# 1.1: (2, 3)
# 1.2: (2, 2)
# 1.3: (3, 2)
# 1.4: (2, 3)
# 1.5: (1, 4)
# 1.6: (4, 1)

# Problem 2: Vector Operations
alpha = 6

print('2.1: ' + str(u + v))
# Matrix([[9, 7, -4, 9]])

print('2.2: ' + str(u - v))
# Matrix([[3, -3, -2, 1]])

print('2.3: ' + str(alpha * u))
# Matrix([[36, 12, -18, 30]])

print('2.4: ' + str(u.dot(v)))
# 51

print('2.5: ' + str(math.sqrt(u.dot(u))))
# 8.602325267042627


# Problem 3: Matrix Operations
try:
    print('3.1: ' + str(A + C))
except:
    print('3.1: Not Defined')
# 3.1: Not Defined

try:
    print('3.2: ' + str(A - Transpose(C)))
except:
    print('3.2: Not Defined')
# 3.2: Matrix([
# [-4, -7, -3],
# [ 3,  6,  4]])


try:
    print('3.3: ' + str(Transpose(C) + 3 * D))
except:
    print('3.3: Not Defined')
# 3.3: Matrix([
# [14, 3, 3],
# [ 2, 7, 9]])


try:
    print('3.4: ' + str(B * A))
except:
    print('3.4: Not Defined')
# 3.4: Matrix([[-1, -5, -1], [2, 7, 4]])


try:
    print('3.5: ' + str(B * Transpose(A)))
except:
    print('3.5: Not Defined')
# 3.5: Not Defined


try:
    print('3.6: ' + str(B * C))
except:
    print('3.6: Not Defined')
# 3.6: Not Defined


try:
    print('3.7: ' + str(C * B))
except:
    print('3.7: Not Defined')
# 3.7: Matrix([[5, -6], [9, -8], [6, -6]])


try:
    print('3.8: ' + str(B**4))
except:
    print('3.8: Not Defined')
# 3.8: Matrix([[1, -4], [0, 1]])


try:
    print('3.9: ' + str(A * Transpose(A)))
except:
    print('3.9: Not Defined')
# 3.9: Matrix([
# [14, 28],
# [28, 69]])


try:
    print('3.10: ' + str(Transpose(D) * D))
except:
    print('3.10: Not Defined')
# 3.10: Matrix([
# [10, -4,  0],
# [-4,  8,  8],
# [ 0,  8, 10]])
