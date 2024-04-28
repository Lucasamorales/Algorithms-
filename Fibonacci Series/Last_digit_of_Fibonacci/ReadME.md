# Last Digit of the Fibonacci Number Calculator

## Problem Statement
This script determines the last digit of the nth Fibonacci number. The Fibonacci sequence, where each number is the sum of the two preceding ones, can grow very large very quickly. For problems that only need the last digit of a Fibonacci number, we can optimize our approach significantly.

**Input**: An integer `n`.  
**Output**: The last digit of the nth Fibonacci number.

**Constraints**:
- $\(0 \leq n \leq 10^6\)$

## Understanding the Problem
In many applications, such as digital signal processing or cryptography, sometimes all that matters is the last digit of a number, not the entire number itself. In these cases, instead of calculating large Fibonacci numbers in full, we can focus solely on their last digits. This not only saves computational time but also space.

## How It Works

### Step 1: Recursive Fibonacci Calculation with Memoization
To avoid recalculating Fibonacci numbers multiple times, we use a technique called memoization (if you read the "FIbonacci_number" folder you´ve probably noticed that this isnt the same way to calculate it, its just another way of doint it, the proevious method works as well!:
```python
memo = {}  # Dictionary to store previously computed Fibonacci numbers

def fib(n: int) -> int:
    if n in memo:
        return memo[n]  # Return the stored result if already computed

    if n <= 2:
        result = 1  # Base cases for the Fibonacci sequence
    else:
        result = fib(n - 1) + fib(n - 2)  # Recursive calculation

    memo[n] = result  # Store the result for future reference
```

-   Explanation: This recursive function efficiently computes Fibonacci numbers by storing the results of all previously computed numbers, reducing the number of computations needed.

### Step 2: Extracting the Last Digit

Once we have the Fibonacci number, we simply take its last digit:

```python

 s = str(result)  # Convert the number to a string
    last = int(s[-1])  # Extract the last character and convert it back to an integer
    return last
````
-   Explanation: Converting the Fibonacci number to a string allows easy access to the last digit, which is then returned.

Complexity
----------

-   Time Complexity: $O(n)$ --- This is due to the memoization technique, which ensures each Fibonacci number up to $n$ is calculated only once.
-   Space Complexity: $O(n)$ --- Space is required to store up to $n$ Fibonacci numbers in the memoization dictionary.
