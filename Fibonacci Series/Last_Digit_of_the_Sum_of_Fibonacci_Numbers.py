"""
Last Digit of the Sum of Fibonacci Numbers
Problem
Compute the last digit of F0 + F1 + ··· + Fn.
Input: An integer n.
Output: The last digit of F0 +F1 +
··· + Fn.
1 + 1 + 2 + 3 + 5 + 8 = 20
Input format. An integer n.
Output format. (F0 + F1 + ··· + Fn) mod 10.
Constraints. 0 ≤ n ≤ 1014
"""

"""
NAIVE APPROACH: =======================================================================
memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n == 0:
        result = 0
    elif n <= 2:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)

    memo[n] = result

    return result


def sumfib(n):
    fib(n)
    counter = 0
    for i in memo.values():
        counter += i

    s = str(counter)
    output = int(s[-1])
    return output
====================================================
"""
def last_digit_of_fibonacci_sum(n):
    # Function to calculate the last digit of Fibonacci
    def last_digit_fib(n):
        if n <= 1:
            return n
        previous, current = 0, 1
        for _ in range(n - 1):
            previous, current = current, (previous + current) % 10
        return current

    # The sum of Fibonacci up to Fn is F(n+2) - 1
    # Calculate the last digit of F(n+2) - 1
    last_digit = last_digit_fib((n + 2) % 60)  # Use the Pisano period to reduce the size
    return (last_digit - 1) % 10  # Ensure the result is non-negative

if __name__ == '__main__':
    n = int(input("Enter the value of n: "))
    print("The last digit of the sum of Fibonacci numbers up to Fn is:", last_digit_of_fibonacci_sum(n))