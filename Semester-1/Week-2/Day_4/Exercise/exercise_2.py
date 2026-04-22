# Task 1: Write recursive 'reverse_string(s)'
# Reverses a string without using [::-1]
# reverse_string("hello") → "olleh"
# Hint: first char goes to the END

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
print(reverse_string("hello"))  # "olleh"
print(reverse_string("Python"))  # "nohtyP"

# Task 2: Write recursive 'count_char(s, char)'
# Counts occurrences of char in string s
# count_char("hello", "l") → 2
# count_char("mississippi", "s") → 4

def count_char(s, char):
    if len(s) == 0:
        return 0
    else:
        count_in_rest = count_char(s[1:], char)
        if s[0] == char:
            return 1 + count_in_rest
        else:
            return count_in_rest
print(count_char("hello", "l"))
print(count_char("mississippi", "s"))

# Task 3: Write recursive 'remove_spaces(s)'
# Removes all spaces from a string
# remove_spaces("hello world") → "helloworld"
# remove_spaces("hi there") → "hithere"

def remove_spaces(s):
    if len(s) == 0:
        return s
    else:
        rest_without_spaces = remove_spaces(s[1:])
        if s[0] == ' ':
            return rest_without_spaces
        else:
            return s[0] + rest_without_spaces
print(remove_spaces("hello world"))
print(remove_spaces("hi there"))