# ============================================
#   RECURSION SHOWCASE 🌀
#   Week 2, Day 4 Project
# ============================================

# ── 1. Factorial ─────────────────────────────
def factorial(n):
    """Return n! recursively."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# ── 2. Fibonacci Sequence (with memorization) ───────────────────

def fibonacci(n, memo={}):
    """Return nth Fibonacci number (memoized)."""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# ── 3. Power Function (x^n) ─────────────────────────────

def power(base, exp):
    """Calculate base^exp recursively."""
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / power(base, -exp)
    else:
        return base * power(base, exp - 1)
    
# ── 4. Palindrome ────────────────────────────

def is_palindrome(s):
    """Check if a string is a palindrome recursively."""
    # Preprocess the string: remove non-alphanumeric characters and convert to lowercase
    s = ''.join(c.lower() for c in s if c.isalnum())
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])
    
# ── 5. Sum of digits ─────────────────────────

def sum_digits(n):
    """Sum all digits of a number recursively."""
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)

# ── Main Menu ─────────────────────────────────

def show_menu():
    print("\n" + "=" * 45)
    print("   RECURSION SHOWCASE 🌀")
    print("=" * 45)
    print("1. Factorial  (n!)")
    print("2. Fibonacci  (nth number)")
    print("3. Power    (base^exp)")
    print("4. Palindrome   (check a word)")
    print("5. Sum of Digits (sum of all digits )")
    print("6. Exit")
    print("=" * 45)
    
def main():
    while True:
        show_menu()
        choice = input("Choose a function (1-6): ")
        if choice == '1':
            n = int(input("Enter n for factorial: "))
            print(f"{n}! = {factorial(n)}")
        elif choice == '2':
            n = int(input("Enter n for Fibonacci: "))
            print(f"Fibonacci({n}) = {fibonacci(n)}")
        elif choice == '3':
            base = float(input("Enter base: "))
            exp = int(input("Enter exponent: "))
            print(f"{base}^{exp} = {power(base, exp)}")
        elif choice == '4':
            word = input("Enter a word to check for palindrome: ")
            if is_palindrome(word):
                print(f"'{word}' is a palindrome!")
            else:
                print(f"'{word}' is not a palindrome.")
        elif choice == '5':
            n = int(input("Enter a number to sum its digits: "))
            print(f"Sum of digits in {n} = {sum_digits(n)}")
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("⚠ Invalid choice. Please try again.")
    
if __name__ == "__main__":
    main()