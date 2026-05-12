# Task 1: Write 'is_valid_email(email)'
# Basic check: has '@', has '.',
# has chars before '@', has chars after '.'
# is_valid_email("test@example.com") → True
# is_valid_email("notanemail")       → False
# is_valid_email("@example.com")     → False

def is_valid_email(email):
    if "@" in email and "." in email:
        parts = email.split("@")
        if len(parts) == 2 and parts[0] and "." in parts[1]:
            domain_parts = parts[1].split(".")
            if domain_parts[0] and domain_parts[-1]:
                return True
    return False
print(is_valid_email("test@example.com"))
print(is_valid_email("notanemail"))
print(is_valid_email("@example.com"))

#Task 2: Write 'title_case_skip(sentence)'
# Title case but skip: a, an, the, in, on, at, of
# title_case_skip("the cat in the hat") → "The Cat in the Hat"

def title_case_skip(sentence):
    words = sentence.split()
    skip_words = ["a", "an", "the", "in", "on", "at", "of"]
    capitalized_words = []
    for index, word in enumerate(words):
        if index == 0 or word.lower() not in skip_words:
            capitalized_words.append(word.title())
        else:
            capitalized_words.append(word)
    return " ".join(capitalized_words)
print(title_case_skip("the cat in the hat"))

# Task 3: Write 'count_word_types(text)'
# Returns dict:
# {'total': n, 'upper': n, 'lower': n, 'mixed': n}
# count_word_types("Hello WORLD python") →
# {'total': 3, 'upper': 1, 'lower': 1, 'mixed': 1}

def count_word_types(text):
    word = text.split()
    total = len(word)
    upper = sum(1 for w in word if w.isupper())
    lower = sum(1 for w in word if w.islower())
    mixed = total - upper - lower
    return {'total': total, 'upper':upper, 'lower':lower, 'mixed':mixed}
print(count_word_types("Hello WORLD python"))