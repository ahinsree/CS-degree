"""Recursion — Functions That Call Themselves"""
"""Recursion is when a function calls itself to solve a smaller version of the same problem."""
# Analogy — Russian Dolls 🪆
# Each doll contains a smaller version of itself
# Until you reach the smallest doll (base case)
# Then you stop opening dolls

# Without recursion — countdown with loop
def countdow_loop(n):
    while n > 0:
        print(n)
        n -= 1
    print("Blastoff! 🚀")
countdow_loop(5)

# Without recursion — countdown with loop
def countdown(n):
    if n == 0:
        print("Blastoff! 🚀")    # BASE CASE — stop here!
    else:
        print(n)
        countdown(n - 1)   # RECURSIVE CASE — call itself
countdown(5)

"""What happens WITHOUT a base case:"""
# ❌ DANGER — infinite recursion!
def no_base(n):
    print(n)
    no_base(n - 1)    # never stops!
# Python will raise: RecursionError: maximum recursion depth exceeded
# Default limit: 1000 calls
import sys
print(sys.getrecursionlimit())   # 1000

"""Every recursive function needs TWO things:
def recursive_function(n):
    # 1. BASE CASE — when to STOP
    if n == 0:
        return "done"

    # 2. RECURSIVE CASE — call itself with SMALLER input
    return recursive_function(n - 1)   
    """