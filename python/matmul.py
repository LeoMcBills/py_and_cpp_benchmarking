import numpy as np
import timeit

def matrix_multiply():
    A = np.random.rand(1000, 1000)
    B = np.random.rand(1000, 1000)
    return np.dot(A, B)

print(timeit.timeit("matrix_multiply()", globals=globals(), number=1000))