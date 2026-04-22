# Task 1: Write recursive 'sum_to(n)'
# Returns sum of all numbers from 1 to n
# sum_to(5) → 15  (1+2+3+4+5)
# sum_to(1) → 1
# sum_to(0) → 0
def sum_to(n):
    if n == 0:
        return 0
    else:
        return n + sum_to(n - 1)
print(sum_to(5))
print(sum_to(1))
print(sum_to(0))

# Task 2: Write recursive 'multiply(a, b)'
# Multiplies two numbers using only addition
# multiply(3, 4) → 12  (3+3+3+3)
# Hint: multiply(3, 4) = 3 + multiply(3, 3)
def multiply(a, b):
    if b == 0:
        return 0
    else:
        return a + multiply(a, b - 1) 
print(multiply(3, 4))
print(multiply(5, 0))

# Task 3: Write recursive 'count_down(n)'
# Prints n, n-1, n-2... 1 then "Done!"
# No loops allowed!
def count_down(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        count_down(n - 1)
count_down(5)