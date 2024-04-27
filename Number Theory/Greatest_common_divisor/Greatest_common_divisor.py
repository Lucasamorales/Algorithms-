"""
Greatest Common Divisor Problem
Compute the greatest common divisor of two
positive integers.
Input: Two positive integers a
and b.
Output: The greatest common divisor of a and b.
"""


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
