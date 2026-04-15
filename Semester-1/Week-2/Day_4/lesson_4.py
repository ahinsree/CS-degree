"""Recursion vs Iteration"""
# SAME problem — two approaches

# ── Iterative sum ────────────────────────────
def iterative_sum(n):
    """Sum 1 to n using a loop."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print(iterative_sum(10))

# ── Recursive sum ────────────────────────────
def recursive_sum(n):
    """Sum 1 to n using recursion."""
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n - 1)
print(recursive_sum(10))

# ✅ Use RECURSION when:
# - Problem is naturally self-similar (trees, graphs)
# - Code is cleaner/more readable recursive
# - Problem defined recursively (factorial, fibonacci)
# - Working with nested data structures

# ✅ Use ITERATION when:
# - Simple counting or accumulation
# - Performance is critical
# - Deep nesting would cause stack overflow
# - Problem is naturally sequential

# General rule:
# "If you can do it cleanly with a loop — use a loop.
#  Use recursion when the recursive solution is
#  significantly cleaner or more natural."