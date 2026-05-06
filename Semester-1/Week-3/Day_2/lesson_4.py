# ── split() — string → list ──────────────────

sentence = "  Hello Python World  "
words = sentence.split()
print(words)  # ['Hello', 'Python', 'World']

# Split specific character
csv = "Alice, Bob, Charlie, David"
names = csv.split(",")
print(names)  # ['Alice', ' Bob', ' Charlie', ' David'] 

# Split with maxsplit limit
text = "One two three four five"
print(text.split(" ", 2))  # ['One', 'two', 'three four five']
print(text.split(maxsplit=2))  # ['One', 'two', 'three four five']

# ── join() — list → string ───────────────────
# join() is the EXACT OPPOSITE of split()
words  = ["Hello", "Python", "World"]

print(" ".join(words))  # "Hello Python World"
print("-".join(words))  # "Hello-Python-World"
print(", ".join(words)) # "Hello, Python, World"

# Rebuild a path
parts = ["home", "ahinsree", "documents"]
print("/".join(parts))  # "home/ahinsree/documents"

# join + split = clean spacing trick!

messy = "too    many   spaces"
cleaned = " ".join(messy.split())
print(cleaned)  # "too many spaces"

# ── strip() — remove characters ──────────────
dirty = "   Hello World  "
print(dirty.strip())        # "Hello World"    ← both sides
print(dirty.lstrip())       # "Hello World   " ← left only
print(dirty.rstrip())       # "   Hello World" ← right only

# Strip specific characters
print("###Hello###".strip("#"))       # "Hello"
print("...Python...".strip("."))      # "Python"
print("  \n\t Hello \t\n  ".strip()) # "Hello" ← all whitespace!

# ── splitlines() ─────────────────────────────
multi = "line1\nline2\nline3\nline4"
print(multi.splitlines())
# ['line1', 'line2', 'line3', 'line4']

# ── Practical: split + join pipeline ─────────
def normalise(text):
    """Remove extra spaces everywhere."""
    return " ".join(text.strip().split())

print(normalise("  Hello   World   "))    # "Hello World"
print(normalise("\t Python \n rocks  "))  # "Python rocks"