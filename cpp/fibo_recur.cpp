#include <iostream>
using namespace std;

int fibonacci_recursive(int); // Prototype

int main() {
    int n = 40;
    cout << "Fibonacci(" << n << ") = " << fibonacci_recursive(n) << endl;
    return 0;
}

int fibonacci_recursive(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2);
}