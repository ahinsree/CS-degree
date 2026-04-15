""" Fibonacci Sequence

Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
Rule: fib(n) = fib(n-1) + fib(n-2)
Base cases: fib(0) = 0, fib(1) = 1

"""
def fibonacci(n):
    """Return the nth Fibonacci number."""
    # Two base cases!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case — calls itself TWICE!
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(10):
    print(f"fib({i}) = {fibonacci(i)}")
    
"""⚠️ The Problem with Naive Fibonacci:"""
import time

start = time.time()
print(fibonacci(35))    # takes several seconds!
end   = time.time()
print(f"Time: {end - start:.2f}s")

# fibonacci(35) calls fibonacci() over 29 MILLION times!
# Same values calculated over and over — very inefficient
# Solution: Memoization (we'll fix this in the exercise!)