"""
Huge Fibonacci Number Problem
Compute the n-th Fibonacci number modulo m.
Input: Integers n and m.
Output: n-th Fibonacci number
modulo m.

Input format. Integers n and m.
Output format. Fn mod m.
Constraints. 1 ≤ n ≤ 1014, 2 ≤ m ≤ 103
.
"""
"""
NAIVE SOLUTION : ======================================================
memo = {}

def fib(n: int) -> int:
    if n in memo:
        return memo[n]

    if n <= 2:
        fibo = 1
    else:
        fibo = fib(n - 1) + fib(n - 2)

    memo[n] = fibo
    return fibo


def modulo(n, m):
    return fib(n) % m
=========================================================================
error : 'RecursionError: maximum recursion depth exceeded in comparison', is due to the recursion limit in Python  
"""

"""
PISANO PERIOD METHOD
"""


def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        # This condition is checked for the first Fibonacci numbers modulo m
        if (previous == 0 and current == 1):
            return i + 1


def fibonacci_modulo(n, m):
    # Get the period of the Fibonacci sequence modulo m
    pisano_period_length = pisano_period(m)
    n = n % pisano_period_length

    if n == 0:
        return 0
    elif n == 1:
        return 1

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


"""
Explanation:
Pisano Period Function (pisano_period): This function computes the length of the cycle for Fibonacci numbers modulo m. 
The maximum length this might need to check is m^2

Fibonacci Modulo Function (fibonacci_modulo): This function first reduces n modulo the length of the Pisano period,
thereby greatly reducing the number of Fibonacci terms needed to be computed.
It then calculates the Fibonacci number iteratively in a way that incorporates the modulo operation to keep numbers manageable.
"""

if __name__ == '__main__':
    n, m = map(int, input("Enter n and m separated by space: ").split())
    print(f"The {n}-th Fibonacci number modulo {m} is {fibonacci_modulo(n, m)}")
