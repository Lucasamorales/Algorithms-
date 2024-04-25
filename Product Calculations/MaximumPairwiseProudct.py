import time
"""
Maximum Pairwise Product Problem
Find the maximum product of two distinct numbers in a sequence of non-negative integers.
Input: An integer n and a sequence of n non-negative integers.
Output: The maximum value
that can be obtained by multiplying two different elements from
the sequence.

Given a sequence of non-negative integers a1
,...,an, compute
max
1≤i,j≤n
ai
· aj
.
Note that i and j should be different, though it may be the case that ai = aj
.
Input format. The first line contains an integer n. The next line contains
n non-negative integers a1
,...,an (separated by spaces).
Output format. The maximum pairwise product.
Constraints. 2 ≤ n ≤ 2 · 10^5;  0 ≤ a1 ,...,an ≤ 2 · 10^5
.
"""
def max_pairwise_product(numbers):
    n = len(numbers)
    index1 = 0
    for i in range(1, n):
        if numbers[i] > numbers[index1]:
            index1 = i
    if index1 == 0:
        index2 = 1
    else:
        index2 = 0

    for i in range(0, n):
        if i != index1 and numbers[i] > numbers[index2]:
            index2 = i

    return numbers[index1] * numbers[index2]


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
