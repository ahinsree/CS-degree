" Practical Recursion "
# Example 1 — Power function
def power(base, exp):
    """Calculate base^exp using recursion."""
    if exp == 0:
        return 1    # BASE CASE: anything to the power of 0 is 1
    else:
        return base * power(base, exp - 1)   # RECURSIVE CASE
print(power(2, 10))   # 1024
print(power(3, 4))    # 81

# Example 2 — Sum of digits
def sum_digits(n):
    """Sum all digits of a number ."""
    if n < 10:
        return n    # BASE CASE: single digit
    else:
        return (n % 10) + sum_digits(n // 10)   # RECURSIVE CASE
print(sum_digits(12345))   # 15
print(sum_digits(999))

# Example 3 — Palindrome checker
def is_palindrome(s):
    """Check if a string is a palindrome recursively."""
    # Preprocess the string: remove non-alphanumeric characters and convert to lowercase
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    # Base case: empty string or single character is a palindrome
    if len(s) <= 1:
        return True
    
    # Recursive case: check if first and last characters are the same
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

# Test the palindrome function
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))  # False
print(is_palindrome("Malayalam"))  # True
print(is_palindrome("Hello"))  # False  
print(is_palindrome("madam"))  # True

# Example 4 — Flatten nested list
def flatten(lst):
    """Flatten a nested list of arbitrary depth."""
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))  # RECURSIVE CASE: flatten the sublist
        else:
            result.append(item)  # BASE CASE: add non-list item to result
    return result
nested_list = [1, [2, [3, 4], 5], 6]
print(flatten(nested_list))  # [1, 2, 3, 4, 5, 6]
