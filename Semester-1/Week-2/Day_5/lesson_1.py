#    Write recursive 'power(base, exp)'
#    power(2, 8) → 256
#    power(3, 0) → 1

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp-1)
print(power(2, 8))
print(power(3, 0))  

#    Write recursive 'is_palindrome(s)'
#    is_palindrome("racecar") → True
#    is_palindrome("hello")   → False

def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False
print(is_palindrome("racecar"))
print(is_palindrome("hello"))

#    Write recursive 'sum_digits(n)'
#    sum_digits(12345) → 15

def sum_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)
print(sum_digits(12345))