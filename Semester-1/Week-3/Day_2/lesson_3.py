# Test Methods
# # Test methods → always return True or False
# ── Character type tests ─────────────────────

print("hello".isalpha())        # True  — all letters
print("hello1".isalpha())       # False - has digit
print("12345".isdigit())        # True  — all digits
print("12.5".isdigit())         # False — dot is not digit
print("hello1".isalnum())       # True  — letters AND digits
print(" ".isspace())            # True  — only spaces
print("".isspace())             # False — empty string
print("".isalpha())             # False — empty string

# ── Case tests ───────────────────────────────

print("HELLO".isupper())        # True
print("hello".islower())        # True
print("Hello World".istitle())  # True  ← every word capitalised
print("Hello world".istitle())  # False ← 'world' not capitalised
print("HeLLo".isupper())        # False ← not ALL upper

# ── Practical: username validator ────────────

def validate_username(username) :
    """Username must be alphanumaric, 3 - 30 chars. """
    if not username.isalnum() :
        return "❌ Only letters and numbers allowed"
    if len(username) < 3 or len(username) > 20:
        return "Length of the user_name between 3 and 20"
    return "✅ Valid Username!"
print(validate_username("ahinsree32"))    # ✅ Valid
print(validate_username("ah"))            # ❌ Too short
print(validate_username("hello world"))   # ❌ has space

# ── Practical: strong password check ─────────

def is_strong_password(pwd):
    """Password needs upper, lower, digit, min 8 chars."""
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    long_enough = len(pwd) >= 8
    return has_upper and has_lower and has_digit and long_enough
print(is_strong_password("Python123"))   # True
print(is_strong_password("python"))      # False — no upper, no digit
print(is_strong_password("PYTHON123"))   # False — no lower
print(is_strong_password("Py1"))         # False — too short