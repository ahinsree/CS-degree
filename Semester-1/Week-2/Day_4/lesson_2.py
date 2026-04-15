"""Factorial is the classic recursion example:
5! = 5 × 4 × 3 × 2 × 1 = 120
4! = 4 × 3 × 2 × 1 = 24
3! = 3 × 2 × 1 = 6
1! = 1
0! = 1  ← by definition"""

def factorial(n):
     # Base case
    if n == 0 or n == 1:
        return 1
    else:
    # Recursive case
        return n * factorial(n - 1)
print(factorial(5))
print(factorial(4))
print(factorial(10))

"""Call Stack Trace — factorial(4):
factorial(4)
  → 4 * factorial(3)
         → 3 * factorial(2)
                → 2 * factorial(1)
                       → returns 1      ← BASE CASE hit!
                → 2 * 1 = 2
         → 3 * 2 = 6
  → 4 * 6 = 24
← returns 24"""