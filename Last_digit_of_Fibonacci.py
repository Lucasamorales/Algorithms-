"""
Last Digit of Fibonacci Number
Last Digit of Fibonacci Number Problem
Compute the last digit of the n-th Fibonacci
number.
Input: An integer n.
Output: The last digit of the n-th
Fibonacci number.
F100 =354224848179
261915075
Input format. An integer n.
Output format. The last digit of Fn.
Constraints. 0 ≤ n ≤ 106
"""
memo = {}


def fib(n: int) -> int:
    if n in memo:
        return memo[n]

    if n <= 2:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)

    memo[n] = result

    s = str(result)

    last = int(s[-1])  # to get the last digit
    return last


if __name__ == "__main__":
    n = int(input())
    print(fib(n))
