sentence = "The quick brown fox jumps over the lazy dog"

# Task 1: Print the first, middle and last character
# Task 2: Print the first word using indexing only (no split!)
#         Hint: find where the first space is
# Task 3: Print True if sentence starts with 'T'
#         and ends with 'g'
# Task 4: Print every character at an even index

print(sentence[0])  # First character
print(sentence[len(sentence) // 2])  # Middle character
print(sentence[-1])  # Last character
first_space_index = sentence.find(' ')
print(sentence[:first_space_index])  # First word
print(sentence.startswith('T') and sentence.endswith('g'))  # Check start and end
print(sentence[::2])  # Every character at an even index