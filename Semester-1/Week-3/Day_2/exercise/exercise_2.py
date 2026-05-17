# Task 1: Clean this messy data into a list
names = "  Alice ,  Bob,Charlie  ,  David  "
# Expected: ['Alice', 'Bob', 'Charlie', 'David']
clear_name = [name.strip() for name in names.split(",")]
print(clear_name)

# Task 2: Given words = ["python", "is", "awesome"]
# a. Join with space
# b. Join with " - "
# c. Join with no separator
words = ["python", "is", "awesome"]
print(" ".join(words))
print(" - ".join(words))
print("".join(words))

# Task 3: Write 'normalize_whitespace(s)'
# normalize_whitespace("  Hello   World  ") → "Hello World"

def normalize_whitespace(s):
    return " ".join(s.split())
print(normalize_whitespace("  Hello   World  "))
print(normalize_whitespace("Python    is   fun"))

# Task 4: Clean this CSV line
csv = "John,  30 , Engineer ,  New York "
# Expected: ['John', '30', 'Engineer', 'New York']

def clean_csv(s):
    return([item.strip() for item in s.split(',')])
    
print(clean_csv("John,  30 , Engineer ,  New York "))