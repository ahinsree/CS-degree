# ✅ Task 1: Lambda Functions

# a. cube(n)
cube = lambda n: n**3
print(cube(3))


# b. is_odd(n)
is_odd = lambda n: n % 2 != 0
print(is_odd(7))

# c. first_char(s)
first_char = lambda s: s[0]
print(first_char("Hello"))

# ✅ Task 2: map() + lambda
prices = [100, 250, 75, 400, 180]

# a + b combined (discount + rounding)
discounted = list(map(lambda p: round(p * 0.9, 2), prices))

print(discounted)

# ✅ Task 3: filter() + lambda

words = ["apple", "hi", "python", "ok",
         "programming", "CS", "algorithm"]

long_words = list(filter(lambda w: len(w) > 4, words))

print(long_words)

# ✅ Task 4: sorted() + lambda

pairs = [(1, 'banana'), (2, 'apple'),
         (3, 'cherry'), (4, 'date')]

sorted_pairs = sorted(pairs, key=lambda x: x[1])

print(sorted_pairs)
# key=lambda x: x[1] → sort by second element

# ✅ Task 5: *args + lambda

def apply_to_all(func, *args):
    return [func(x) for x in args]

result = apply_to_all(lambda x: x**2, 1, 2, 3, 4, 5)

print(result)