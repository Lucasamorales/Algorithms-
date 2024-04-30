# Last Digit of the Sum of Squares of Fibonacci Numbers Calculator

## Problem Statement
This script calculates the last digit of the sum of the squares of the Fibonacci numbers from $\( F_0^2 \)$ to $\( F_n^2 \)$. This problem extends the concept of Fibonacci numbers into squares, which can grow exponentially larger, thus needing an efficient computational method.

**Input**: An integer `n`.  
**Output**: The last digit of the sum $\( F_0^2 + F_1^2 + \ldots + F_n^2 \)$ modulo 10.

**Constraints**:
- $\(0 \leq n \leq 10^{14}\)$

## Understanding the Problem
Calculating each Fibonacci number and then squaring it can be computationally intensive, especially as the sequence grows. However, a beautiful identity in Fibonacci sequences states that the sum of the squares of the first $\( n \)$ Fibonacci numbers equals $\( F_n \times F_{n+1} \)$. This identity dramatically simplifies our task to just computing two consecutive Fibonacci numbers and multiplying them.


### Numerical Example

Let's consider \( n = 5 \) to demonstrate this calculation.

- **The first six Fibonacci numbers are:**
 0, 1, 1, 2, 3, 5 (including $\( F_0 \)$ to $\( F_5 \))$

- **The squares of these numbers are:**
  $\(0^2, 1^2, 1^2, 2^2, 3^2, 5^2 = 0, 1, 1, 4, 9, 25\)$

- **Normally, the sum of these squares would be:**
  $\(0 + 1 + 1 + 4 + 9 + 25 = 40\)$

**Using the Fibonacci identity:**
- $\( F_5 = 5 \)$
- $\( F_6 = 8 \)$ (the next Fibonacci number)

- **According to the identity, $\( F_5 \times F_6 = 5 \times 8 = 40 \)$**

Thus, using the identity $\( F_n$ $\times$ $F_{n+1}$ \), we find the sum of the squares of the first $\( n \)$ Fibonacci numbers quickly and without needing to compute each square individually. This dramatically reduces the complexity, especially as $\( n \)$ increases.


## How It Works

### Efficient Computation Using Pisano Period
The Pisano Period helps in reducing the number of computations when dealing with modular arithmetic of Fibonacci numbers. For modulo 10, the Fibonacci sequence properties repeat every 60 numbers:
```python
def last_digit_of_squares_fibonacci_sum(n: int) -> int:
    if n <= 1:
        return n  # Directly return n for 0 or 1 as their squares are themselves
    n = n % 60  # Reduce n modulo 60 due to the Pisano period

    previous, current = 0, 1
    for _ in range(2, n + 2):  # Compute up to F_{n+1}
        previous, current = current, (previous + current)
    
    result = (previous * current) % 10  # Compute the product and then take modulo 10
    return result
```
-   Explanation: Instead of summing squares directly, we compute $Fn$​ and $Fn+1$​, then find their product modulo 10. This method only requires computing Fibonacci numbers, avoiding large square computations entirely.

Complexity
----------

-   Time Complexity: $O(1)$ --- With the use of the Pisano period reduction, we ensure a maximum of 60 iterations, regardless of the size of �n.
-   Space Complexity: $O(1)$ --- Constant space is used, irrespective of the input size.
