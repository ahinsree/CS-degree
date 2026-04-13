# Task 1: Write a function 'multiply_all(*args)'
# Multiplies ALL numbers passed to it
# multiply_all(2, 3)       → 6
# multiply_all(2, 3, 4)    → 24
# multiply_all(1, 2, 3, 4, 5) → 120

def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result
print(multiply_all(2, 3))
print(multiply_all(2, 3, 4))
print(multiply_all(1, 2, 3, 4, 5))

# Task 2: Write 'find_largest(*args)'
# Returns the largest number from any number of args
# find_largest(3, 1, 4, 1, 5, 9) → 9
# Hint: use max() or write your own logic

def find_largest(*args):
    largest = args[0]
    for num in args:
        if num > largest:
            largest = num
    return largest
print(find_largest(3, 1, 4, 1, 5, 9))

# Task 3: Write 'print_all(separator, *args)'
# Prints all args separated by the separator
# print_all(" | ", "Alice", "Bob", "Charlie")
# → Alice | Bob | Charlie

def print_all(seperator, *args):
    print(seperator.join(args))
print_all(" | ", "Alice", "Bob", "Charlie")