import timeit

# Iterative Fibonacci
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(timeit.timeit("fibonacci_iterative(12)", globals=globals(), number=1000))