import numpy as np

def matrix_multiply():
    A = np.random.rand(1000, 1000)
    B = np.random.rand(1000, 1000)
    return np.dot(A, B)