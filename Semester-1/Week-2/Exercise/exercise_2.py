# Task 1: Write 'build_sentence(**kwargs)'
# Uses name, verb, object from kwargs to build a sentence
# build_sentence(name="Alice", verb="loves", object="Python")
# → "Alice loves Python"

def build_sentence(**kwargs):
    name = kwargs.get("name", "Unknown")
    verb = kwargs.get("verb", "Unknown")
    object = kwargs.get("object", "Unknown")
    return f"{name} {verb} {object}"
print(build_sentence(name="Alice", verb="loves", object="Python"))

# Task 2: Write 'filter_adults(**people)'
# people = name: age pairs
# Prints only people aged 18 or above
# filter_adults(Alice=22, Bob=15, Charlie=30, David=17)
# → Alice: 22
# → Charlie: 30
def filter_adults(**people):
    for name, age in people.items():
        if age >= 18:
            print(f"{name}: {age}")
filter_adults(Alice=22, Bob=15, Charlie=30, David=17)

# Task 3: Write 'merge_configs(default, **overrides)'
# Takes a default dict and any number of overrides
# Returns merged config
# default = {"theme": "light", "lang": "en", "size": 12}
# merge_configs(default, theme="dark", size=16)
# → {"theme": "dark", "lang": "en", "size": 16}

def merge_configs(default, **overrides):
    merged = {**default, **overrides}            #Dictionary Unpacking {**default, **overrides}
    return merged
default = {"theme": "light", "lang": "en", "size": 12}
print(merge_configs(default, theme="dark", size=16))    

"""# What happens inside the dictionary literal:
{**default, **overrides}

# Is equivalent to:
{"theme": "light", "lang": "en", "size": 12, "theme": "dark", "size": 16}

Duplicate Key Resolution
When duplicate keys exist, later values override earlier ones:

# Order of operations:
1. {"theme": "light", "lang": "en", "size": 12}  # From default
2. Then add {"theme": "dark", "size": 16}        # From overrides

# Final result:
{"theme": "dark", "lang": "en", "size": 16}

"""

"""Key Concepts:

1. Dictionary Unpacking (**dict)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

combined = {**dict1, **dict2}
# Result: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

2. Overriding Behavior (Rightmost wins)

default = {"x": 10, "y": 20}
overrides = {"x": 99}

result = {**default, **overrides}  # {'x': 99, 'y': 20}
result2 = {**overrides, **default} # {'x': 10, 'y': 20} (different!)

3. Multiple Dictionary Unpacking
python
user_config = {"theme": "dark"}
app_defaults = {"lang": "en", "size": 12}
system_defaults = {"size": 10, "debug": False}

final = {**system_defaults, **app_defaults, **user_config}
# Result: {'size': 12, 'debug': False, 'lang': 'en', 'theme': 'dark'}

Alternative Ways to Merge Dictionaries:

# Method 1: Using | operator (Python 3.9+)
merged = default | overrides

# Method 2: Using copy() and update()
merged = default.copy()
merged.update(overrides)

# Method 3: Using dict() constructor
merged = dict(default, **overrides)

# Method 4: Dictionary unpacking (shown in code)
merged = {**default, **overrides}

"""