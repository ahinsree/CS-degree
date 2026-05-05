
# ── The 5 case methods ──────────────────────────────────────────────────────────────────────

text = "hello, python world! "
print(text.upper())  # Convert to uppercase
print(text.lower())  # Convert to lowercase
print(text.title())  # Convert to title case
print(text.capitalize())  # Capitalize the first character
print(text.swapcase())  # Swap case of each character

# ── See the difference clearly ───────────────────────────────────────────────────────────

mixed = "hElLo WoRlD"
print(mixed.upper())  # Output: HELLO WORLD
print(mixed.lower())  # Output: hello world
print(mixed.title())  # Output: Hello World
print(mixed.capitalize())  # Output: Hello world
print(mixed.swapcase())  # Output: HeLlO wOrLd

# ── title() vs capitalize() ──────────────────
sentence = "the quick brown fox"
print(sentence.title())      # "The Quick Brown Fox" ← every word
print(sentence.capitalize()) # "The quick brown fox" ← first only

# ── Case-insensitive comparison ───────────────
user_input = "PyThOn"
if user_input.lower() == "python":
    print("✅ Correct!")
else:
    print("❌ Incorrect!")

## ── casefold() — stronger than lower() ───────
# Used for international text
german = "Straße"
print(german.lower())     # "straße"
print(german.casefold())  # "strasse" ← more aggressive normalisation
# Use casefold() for international comparisons
# Use lower() for regular English comparisons