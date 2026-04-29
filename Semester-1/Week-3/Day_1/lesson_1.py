"""📘 LESSON 1 — String Basics & Creation"""

# Strings are sequences of characters
# Created with single, double, or triple quotes
s1 = 'Hello'
s2 = "world"
s3 = '''This is a multi-line
string.'''
s4 = """Also multi-line"""

# String with special characters
path    = "C:\\Users\\Ahinsree"    # escaped backslash
tab     = "col1\tcol2"             # tab character
newline = "line1\nline2"           # newline character
raw     = r"C:\Users\Ahinsree"     # raw string — no escaping

print(path)
print(tab)
print(newline)
print(raw)

# String properties

name = "Ahinsree"
print(len(name))          # length of string
print(type(name))         # type of variable
print(name[0])           # indexing (first character)

# Strings are sequences — they support:

print("Ahin" + "sree")  # concatenation
print("Ha" * 3)        # repetition
print("A" in "Ahinsree") # membership test
print("Z" not in "Ahinsree") # negative membership test