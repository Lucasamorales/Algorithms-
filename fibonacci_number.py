"""
Fibonacci Number Problem
Compute the n-th Fibonacci number.
Input: An integer n.
Output: n-th Fibonacci number.
Fn = Fn−1 + Fn−2
Fibonacci numbers are defined recursively:
Fn =



n if n is 0 or 1
Fn−2 + Fn−1
if n ≥ 2
resulting in the following recursive algorithm:
Fibonacci(n):
if n ≤ 1:
return n
else:
return Fibonacci(n − 2) + Fibonacci(n − 1)
Input format. An integer n.
Output format. Fn.
Constraints. 0 ≤ n ≤ 45.
"""
"""
Memoization: =======================================================
memo = {}
def fib(n: int) -> int:
    if n in memo:
        return memo[n]

    if n <= 2:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)

    memo[n] = result
    return result
==================================================================
"""
"""
ITERATIVE(faster): 
"""
def fib(n: int) -> int:
    if n <= 1:
        return n

    previous, current = 0, 1

    for i in range(2, n + 1):
        previous, current = current, (previous + current)

    return current


if __name__ == '__main__':
    _ = int(input())
    print(fib(_))
