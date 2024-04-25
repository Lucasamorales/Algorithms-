Maximum Pairwise Product 
===================================

Description
-----------

This script finds the maximum product of two distinct numbers in a given list of non-negative integers. The maximum pairwise product is the largest product that can be obtained by multiplying any two different numbers from the list.

How It Works
------------

Here's how the script operates:

1.  Initialization: It starts by identifying the two largest numbers in the list.
2.  Calculation: It multiplies these two numbers.
3.  Result: The script outputs the result of this multiplication, which is the maximum pairwise product.

Complexity
----------

-   Time Complexity: O(n). The script efficiently finds the two largest numbers with a single loop through the list.
-   Space Complexity: O(1). Uses a fixed amount of space to store the two largest numbers, regardless of the input size.

Example Usage
-------------

Suppose you have a list of numbers: [1, 2, 3, 4, 5]. The maximum pairwise product is obtained by multiplying 4 and 5.

- Input: 1 2 3 4 5 
- Output: 20
