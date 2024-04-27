"""
Least Common Multiple Problem
Compute the least common multiple of two positive integers.
Input: Two positive integers a
and b.
Output: The least common multiple of a and b.

The least common multiple LCM(a,b) of two positive integers a and b is
the smallest integer that is divisible by both a and b.
"""

def lcm(a,b):
    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)

    return int(a*b/gcd(a,b))

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm(a,b))
