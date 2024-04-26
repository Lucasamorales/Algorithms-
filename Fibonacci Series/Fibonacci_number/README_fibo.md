# Fibonacci Number Calculator

## Problem Statement
This script calculates the nth Fibonacci number. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting with 0 and 1.

**Input**: An integer `n`.  
**Output**: The nth Fibonacci number.

The Fibonacci numbers are defined recursively as follows:
 ```math
  F_n = \begin{cases} n & \text{if } n = 0 \text{ or } 1\\ F_{n-1} + F_{n-2} & \text{if } n \geq 2 \end{cases} 
```
**Constraints**:
- $0 \leq n \leq 45$

## Understanding the Problem
The Fibonacci sequence is not only a fundamental mathematical sequence but also a common problem in computer science used to test understanding of recursion and dynamic programming. The challenge is to compute the $nth$ number in this sequence efficiently:

1. **Base Cases**: Identify if the input is 0 or 1, as these have predefined values in the sequence.
2. **Recursive Growth**: Each subsequent number is the sum of the two preceding ones. This can be solved recursively, but such an approach is not efficient for higher numbers due to repeated calculations.
3. **Iterative Solution**: Use an iterative approach to build the sequence from the bottom up, which is more efficient.

## How It Works

### Step 1: Handle Base Cases
```python
if n == 0:
    return 0
elif n == 1:
    return 1
```
-   Explanation: Directly return 0 or 1 if `n` is 0 or 1 respectively.

### Step 2: Iteratively Compute Fibonacci Number

```python
a, b = 0, 1
for i in range(2, n+1):
    a, b = b, a + b
return b
````

-   Explanation: Initialize the first two Fibonacci numbers and use a loop to compute up to the nth number, updating the last two numbers iteratively.

Complexity
----------

-   Time Complexity: $O(n)$ --- The time complexity is linear, as it involves a single loop from 2 to `n`.
-   Space Complexity: $O(1)$ --- Uses a constant amount of space, storing only the last two numbers at any point.

Example Usage
-------------

Input: `10`\
Output: `55` (The 10th Fibonacci number)

To run the script:

```bash


python fibonacci_number.py
```

Input the integer `n` when prompted.
