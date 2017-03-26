# Matrix Algebra

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


# Problem 2: Vector Operations
alpha = 6

print('2.1: ' + str(u + v))
print('2.2: ' + str(u - v))
print('2.3: ' + str(alpha * u))
print('2.4: ' + str(u.dot(v)))
print('2.5: ' + str(math.sqrt(u.dot(u))))


# Problem 3: Matrix Operations
try:
    print('3.1: ' + str(A + C))
except:
    print('3.1: Not Defined')

try:
    print('3.2: ' + str(A - Transpose(C)))
except:
    print('3.2: Not Defined')

try:
    print('3.3: ' + str(Transpose(C) + 3 * D))
except:
    print('3.3: Not Defined')

try:
    print('3.4: ' + str(B * A))
except:
    print('3.4: Not Defined')

try:
    print('3.5: ' + str(B * Transpose(A)))
except:
    print('3.5: Not Defined')

try:
    print('3.6: ' + str(B * C))
except:
    print('3.6: Not Defined')

try:
    print('3.7: ' + str(C * B))
except:
    print('3.7: Not Defined')

try:
    print('3.8: ' + str(B**4))
except:
    print('3.8: Not Defined')

try:
    print('3.9: ' + str(A * Transpose(A)))
except:
    print('3.9: Not Defined')

try:
    print('3.10: ' + str(Transpose(D) * D))
except:
    print('3.10: Not Defined')
