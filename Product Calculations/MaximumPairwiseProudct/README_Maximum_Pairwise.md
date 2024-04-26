
# Maximum Pairwise Product Calculator

## Problem Statement
This script addresses the "Maximum Pairwise Product Problem," where the objective is to find the maximum product of two distinct numbers in a sequence of non-negative integers.

**Input**: An integer `n` followed by a sequence of `n` non-negative integers.  
**Output**: The maximum value that can be obtained by multiplying two different elements from the sequence.

Given a sequence of non-negative integers $\(a_1, a_2, ..., a_n\)$, compute $\(\max_{1 \leq i, j \leq n} a_i \cdot a_j\)$ where $\(i\)$ and $\(j\)$ should be different. Note that it may be the case that $\(a_i = a_j\)$.

**Constraints**:
- $\(2 \leq n \leq 200,000\)$
- $\(0 \leq a_1, ..., a_n \leq 200,000\)$

## Understanding the Problem
When faced with the challenge of finding the maximum pairwise product in a list, the simplest approach is to look for the two biggest numbers because multiplying them will naturally give the highest product. Here’s a straightforward way to think about this:

1. **Identify the Largest**: Scan through the list to find the largest number. This will be one part of our maximum product.
2. **Identify the Second Largest**: Look for the second largest number that can be multiplied with the first to maximize the output.
3. **Consider Edge Cases**: Ensure that these two numbers are distinct or that the same number doesn’t get selected twice unless it appears more than once in the list.

By focusing on these two numbers, we simplify the problem and avoid unnecessary computations involving smaller numbers, which won’t yield a higher product.


How It Works
------------

### Step 1: Initialization and Finding the Largest Number

```python 
index1 = 0  # Start by assuming the first element is the largest
for i in range(1, n):  # Loop through the list starting from the second element
    if numbers[i] > numbers[index1]:
        index1 = i  # Update index1 if a larger number is found
```
-   Explanation: Initialize `index1` to the first element and iterate through the list to find the largest number.

### Step 2: Finding the Second Largest Number


```python 
if index1 == 0:
    index2 = 1  # Set index2 to the first element if index1 is 0
else:
    index2 = 0  # Otherwise, start with the first element
for i in range(0, n):  # Iterate over the entire list
    if i != index1 and numbers[i] > numbers[index2]:
        index2 = i  # Update index2 if a larger second number is found`
```
-   Explanation: After the largest number is identified, find the second largest ensuring it's distinct from the largest.

### Step 3: Calculate the Maximum Pairwise Product
```python 

max_product = numbers[index1] * numbers[index2]  # Multiply the two largest numbers
```

-   Explanation: The product of the two largest numbers represents the maximum pairwise product.

Complexity
----------

-   Time Complexity: $O(n)$ --- Two passes through the list are required.
-   Space Complexity: $O(1)$ --- Minimal additional storage is needed.

Example Usage
-------------

Input: `5 1 2 3 4 5`\
Output: `20` (because the largest numbers are 4 and 5 and their product is 20).

To run the script:

```bash

python MaximumPairwiseProduct.py
```
Enter the list of numbers when prompted, separated by spaces.
