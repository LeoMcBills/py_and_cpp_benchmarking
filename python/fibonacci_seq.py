import timeit

'''
Description: Calculate the nth fibonacci number using both iterative and recursive approaches.
Why: This tests the language's function call overhead, recursion depth, and the effieciency of loop handling
'''

def fibo_recursive(n):
    if n <= 1:
        return n
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)

print(timeit.timeit("fibo_recursive(12)", globals=globals(), number=1000))