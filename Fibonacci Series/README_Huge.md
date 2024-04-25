Huge Fibonacci Number 
================================

Description
-----------

This script calculates the nth Fibonacci number modulo m. This is particularly useful when n is very large and direct computation of the Fibonacci number would be infeasible due to the rapid growth of the sequence.

How It Works
------------

1.  Initialization: It starts with the first two numbers of the Fibonacci sequence: 0 and 1.
2.  Modulo Computation: As it calculates each new Fibonacci number, it immediately applies the modulo operation with m to keep the numbers manageable.
3.  Result: The script outputs the nth Fibonacci number modulo m after completing the loop.

Complexity
----------

-   Time Complexity: O(n). It iterates through n to compute the Fibonacci number, applying the modulo operation to each term.
-   Space Complexity: O(1). It uses a constant amount of space to store only the two most recent numbers in the sequence.

Example Usage
-------------

- Input: n = 10, m = 3
- Output: 2
