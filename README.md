# py_and_cpp_benchmarking


When testing the performance of programming languages, several benchmark programs can be used to evaluate their efficiency in various scenarios. Here are some common programs and tasks that are typically employed:
Common Benchmark Programs

- Sorting Algorithms
Implementations of popular sorting algorithms (e.g., QuickSort, MergeSort, BubbleSort) can be used to measure how quickly each language handles data sorting.
Mathematical Computations
Tasks like calculating Fibonacci numbers or performing matrix multiplications are standard benchmarks. These tests help assess performance in handling arithmetic operations and recursion.

- File I/O Operations
Programs that read from and write to large files (e.g., processing a file with one billion rows) can reveal how well a language manages I/O operations. For example, a Java program that calculates min, mean, and max temperatures from a massive dataset is currently being tested 1
        .
- Algorithmic Challenges
Problems like the 15-Queens Problem or the Sudoku Solver are often used because they involve complex logic and can demonstrate the efficiency of different algorithms across languages 1
        .
- Prime Number Generation
Programs that generate prime numbers up to a certain limit can be useful for testing computational efficiency and algorithmic optimization.
    
- String Manipulation
Tasks involving heavy string processing, such as concatenation or pattern matching, help evaluate how well languages handle text data.
    
- Recursive Functions
Implementing recursive algorithms (like calculating factorials or traversing trees) can provide insights into how languages manage stack memory and recursion depth.
    
- Web Server Performance
Simple web servers can be set up to handle requests and measure response times, which is particularly relevant for languages used in web development 6.

Performance Measurement Tools
To effectively measure performance across different programming languages, consider using the following tools:

Benchmarking Libraries: Libraries like hyperfine or Google Benchmark can automate timing and provide statistical analysis of run times.
Profilers: Tools such as gprof or valgrind help analyze where time is spent within your programs.
Custom Scripts: Writing scripts that utilize /usr/bin/time for measuring execution time and memory usage can provide detailed insights into performance characteristics 4


## Tools for test performance
## For Python3
1. **`timeit`**
```python
import timeit

def exp():
    # Code
    pass

print(timeit.timeit("exp()", globals=globals(), number=1000))
```

2. **Profilers:**
- `cProfile`: It is a built-in profiler for Python that provides a detailed report of time taken by various parts of the program.
```bash
python -m cProfile test_script.py
```

## For C++
- The `chrono` library in C++ provides high-precision time points and durations, which is useful for benchmarking code.

* Example code:
```c++
#include <iostream>
#include <chrono>

void example_function() {
        // code statement
}

int main() {
        auto start = std::chrono::high_resolution_clock::now();
        example_function();
        auto end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double>duration = end - start;
        std::cout << "Execution Time: " << duration.count() << " seconds\n";
        return 0;
}
```