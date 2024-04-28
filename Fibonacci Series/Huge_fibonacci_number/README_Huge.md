# Huge Fibonacci Number Modulo Calculator

## Problem Statement
This script calculates the nth Fibonacci number modulo m. This problem is a common one in number theory and algorithms, particularly in applications that involve periodicity in modular arithmetic.

**Input**: Two integers `n` and `m`.  
**Output**: The nth Fibonacci number modulo m.

**Constraints**:
- $\(1 \leq n \leq 10^{14}\)$
- $\(2 \leq m \leq 10^3\)$

## Understanding the Problem
Computing large Fibonacci numbers directly is inefficient and impractical due to rapid growth. Using modular arithmetic can simplify the problem significantly, particularly with the help of the Pisano Period, which is the period with which the sequence of Fibonacci numbers taken modulo `m` repeats. 

you can check it out here : https://en.wikipedia.org/wiki/Pisano_period

## How It Works

### Step 1: Calculate Pisano Period
The Pisano Period is crucial for reducing the problem size:
```python
def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m * m):  # Check up to m*m as that's the upper bound for the period length
        previous, current = current, (previous + current) % m  # Update the Fibonacci sequence mod m
        if (previous == 0 and current == 1):  # The sequence starts repeating with 0, 1
            return i + 1  # Return the length of the Pisano period
```
-   Explanation: Computes the length of the cycle of Fibonacci numbers modulo `m`. The maximum length that might need to be checked is $m^2$.

### Step 2: Reduce `n` Modulo Pisano Period

Reduce `n` using the length of the Pisano period to minimize the number of computations:

```python

def fibonacci_modulo(n, m):
    pisano_period_length = pisano_period(m)  # Get the Pisano period for m
    n = n % pisano_period_length  # Reduce n modulo the Pisano period length
```

### Step 3: Compute Fibonacci Modulo

Compute the reduced Fibonacci number iteratively incorporating modulo operation:

```python

  if n == 0:
      return 0  # Return 0 if reduced n is 0
  elif n == 1:
      return 1  # Return 1 if reduced n is 1

  previous, current = 0, 1
  for _ in range(n - 1):  # Only compute up to the reduced n
      previous, current = current, (previous + current) % m  # Fibonacci calculation with modulo

  return current  # The nth Fibonacci number modulo m
```

-   Explanation: After reducing `n`, the Fibonacci number is computed in a loop that takes advantage of the Pisano period.

Complexity
----------

-   Time Complexity: $O(m2)$ --- The dominant factor is the calculation of the Pisano period.
-   Space Complexity: $O(1)$ --- Uses a constant amount of space.
