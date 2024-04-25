"""
Last Digit of the Sum of Squares of Fibonacci Numbers Problem
Input: An integer n.
Output: The last digit of F
2
0 +F
2
1 +
··· + F
2
n
.
"""
"""
NAIVE SOLUTION: ==========================================================
def last_digit_of_squares_fibonacci_sum(n):
    # Function to calculate the last digit of Fibonacci
    def last_digit_fib(n):
        if n <= 1:
            return n
        previous, current = 0, 1
        for _ in range(n - 1):
            previous, current = current, (previous ** 2 + current ** 2) % 10
        return current

    # The sum of Fibonacci up to Fn is F(n+2) - 1
    # Calculate the last digit of F(n+2) - 1
    last_digit = last_digit_fib((n + 2) % 60)  # Use the Pisano period to reduce the size
    return (last_digit - 1) % 10  # Ensure the result is non-negative

=============================================================================

this doesnt work beacuse of memory 
"""

"""
The first equation to consider is that: F^2_1 + F^2_2 + ... + F^2_N =  F_N * F_N+1

Hence instead of calculating a Fibonacci squares in each step (which take too long as can be predicted) we only need nth and (n+1)th Fibonacci values.

But also, it is unpractical to calculate the values that are higher than the Pisano period (which is simply the period that the remainder value repeats itself).
Since we are only looking for the last digit, we can consider the problem as the module 10 of the calculated square sum of the Fibonacci values. 
And since Pisano period for modulo 10 is 60, we can use this value here.

That is why, for any given input number of n, if we take the modulo 60 of n and calculate the sum of the squares, 
we would decrease the computational time effectively.

And at the end, by taking the modulo 10 of the calculated value, we can return the last digit.
"""


def last_digit_of_squares_fibonacci_sum(n: int) -> int:
    if n <= 1:
        return n
    n = n % 60

    previous, current = 0, 1
    for _ in range(2, n + 2):  # Iterate until n+2, since we are looking for F_N + F_{N+1}
        previous, current = current, (previous + current) # Calculate the current Fibonacci value

    result = (previous * current) % 10
    return result


if __name__ == '__main__':
    n = int(input("Enter the value of n: "))
    print("The last digit of the sum of squares of Fibonacci numbers up to Fn is:",
          last_digit_of_squares_fibonacci_sum(n))
