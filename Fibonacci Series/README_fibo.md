Fibonacci Number 
===========================

Description
-----------

This script calculates a specific entry in the Fibonacci sequence. The Fibonacci sequence is a series of numbers where the first two numbers are 0 and 1, and each subsequent number is the sum of the two preceding ones. This means the sequence starts like this: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.

The script uses a simple, iterative method to find the nth number in this sequence, where n is a number you provide. For example, if you ask for the 10th number, the script will return 55. 

There is also a commented section where i use the memoization method! 

How It Works
------------

Here's a breakdown of the steps the script takes:

1.  Initialization: It starts with the first two numbers of the Fibonacci sequence: 0 and 1.
2.  Iteration: The script loops, each time calculating the next number in the sequence by adding the two most recent numbers.
3.  Result: After completing the loop n times, the script outputs the nth Fibonacci number.
Complexity
----------

-   Time Complexity: O(n), as it iterates once through n steps.
-   Space Complexity: O(1), using only a constant amount of space to store intermediate results.

Example Usage
-------------

- Input: 10 
- Output: 55
