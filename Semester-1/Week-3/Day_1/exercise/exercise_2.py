text = "Hello, Python world!"

# Task 1: Extract "Python" using slicing
#         Hint: find its position first using .index()

start_index = text.index("Python")
end_index = start_index + len("Python")
print(text[start_index:end_index])  # Output: Python

# Task 2: Reverse the entire string using slicing
reversed_text = text[::-1]
print(reversed_text)  # Output: !dlrow nohtyP ,olleH

# Task 3: Extract every 3rd character
every_third_char = text[::3]
print(every_third_char)  # Output: H,P o l!

# Task 4: Print the string backwards with only
#         uppercase letters — use slicing + methods

backwards_upper = text[::-1].upper()
print(backwards_upper)  # Output: !DLROW NOHTYP ,OLLEH

# Task 5: Extract the last word "World" using negative slicing
last_word = text[-6:-1]  # "world" is 5 characters + 1 for the exclamation
print(last_word)  # Output: world