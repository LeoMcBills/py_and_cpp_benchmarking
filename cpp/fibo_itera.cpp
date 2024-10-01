#include <iostream>
using namespace std;

int fibonacci_iterative(int);

int main() {
    int n = 12;
    cout << "Fibonacci(" << n << ") = " << fibonacci_iterative(n) << endl;
    return 0;
}

int fibonacci_iterative(int n) {
    int a = 0, b = 1, c;
    for (int i = 1; i < n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}