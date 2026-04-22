# The naive fibonacci is SLOW for large n
# Fix it using memoization — cache already computed values

# Hint: use a dictionary to store results

def fibonacci_memo(n, memo={}):
    # check if already computed
    if n in memo:
        return memo[n]
    
    # Base cases 
    if n == 0: return 0
    if n == 1: return 1
    
    # Compute and store in memo
    result = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    memo[n] = result
    print(memo)
    return result
# Test the speed difference!
import time
start = time.time()
print(fibonacci_memo(35)) # slow version
print(f"Slow: {time.time() - start:.4f}s")

start = time.time()
print(fibonacci_memo(35)) # fast version
print(f"Fast: {time.time() - start:.4f}s")