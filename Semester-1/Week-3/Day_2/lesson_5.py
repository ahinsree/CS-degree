# ── replace() ────────────────────────────────
text = "I love cats. Cats are great. My cat is cute."

#Replace all occurrence
new = text.replace("cat", "dog")
print(new)  # "I love dog. Cat are great. My dog is cute."
            # ⚠️ case sensitive — "Cats" NOT replaced!

# Replace with count limit
print(text.replace("cat", "dog", 1))  # "I love dog. Cat are great. My cat is cute."
# Only replace first cat

# Case-insensitive replace — chain lower first
lower =  text.lower().replace("cat", "dog")
print(lower)

# ── Method chaining ──────────────────────────
# Each method returns a NEW string → can chain
result = "  Hello, World!  ".strip().lower().replace(",", "")
print(result)  # "hello world!"

title = "  the quick brown fox  ".strip().title()
print(title)    # "The Quick Brown Fox"

# Long chain — format a username
raw_input = "  AHINSREE Bhargavan  "
username  = raw_input.strip().lower().replace(" ", "_")
print(username)   # "ahinsree_bhargavan"

# ── Pattern 1: Clean user input ──────────────
def clean_input(s):
    """Normalise any user input."""
    return " ".join(s.strip().lower().split())

print(clean_input("  Hello   WORLD  "))   # "hello world"

# ── Pattern 2: Parse CSV line ────────────────
def parse_csv(line):
    """Parse CSV with messy spacing."""
    return [val.strip() for val in line.split(",")]

line = "Alice , 32 , Alappuzha , Python"
print(parse_csv(line))
# ['Alice', '32', 'Alappuzha', 'Python']

# ── Pattern 3: Word frequency ────────────────
def word_frequency(text):
    """Count frequency of each word."""
    words = text.lower().split()
    freq  = {}
    for word in words:
        word       = word.strip(".,!?;:")
        freq[word] = freq.get(word, 0) + 1
    return dict(sorted(freq.items(),
                        key=lambda x: x[1],
                        reverse=True))

sample = "the cat sat on the mat the cat"
print(word_frequency(sample))
# {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}.    

# ── Pattern 4: Slug generator ────────────────
def to_slug(title):
    """Convert a title to URL slug."""
    return title.strip().lower().replace(" ", "-")

print(to_slug("Hello Python World"))
# "hello-python-world"