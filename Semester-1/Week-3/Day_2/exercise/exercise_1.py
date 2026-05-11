# Task 1: Without using split():
# a. Capitalise properly (title case)
# b. Check if "quick" is in the sentence
# c. Count how many times 'o' appears
# d. Find the index of "brown"
# e. Check if it ends with "fox"

sentence = "the quick brown fox"
print(sentence.title())
print("quick" in sentence)
print(sentence.count("o"))
print(sentence.find("brown"))
print(sentence.endswith("fox"))

# Task 2: Write 'count_words_with(text, letter)'
# Counts words starting with a given letter
# count_words_with("hello have happy world", "h") → 3

def count_words_with(text, letter):
    words = text.split()
    count = 0
    for word in words:
        if word.startswith(letter):
            count += 1
    return count
print(count_words_with("hello have happy world", "h"))  # Output: 3

# Task 3: Write 'most_common_char(s)'
# Returns most frequent character (ignore spaces)
# most_common_char("hello") → 'l'

def most_common_char(s):
    # Initialize frequency dictionary
    char_count ={}
    
    # Count occurrences of each character, excluding spaces
    for char in s:
        if char != " ":
            char_count[char] = char_count.get(char, 0) + 1
            
    # If the string was empty or only spaces, return None
    if not char_count:
        return None
    
    # Find the key with maximum value
    return max(char_count, key=char_count.get)

# Test cases
print(most_common_char("hello"))        # Output: 'l'
print(most_common_char("apple pie"))    # Output: 'p'

    