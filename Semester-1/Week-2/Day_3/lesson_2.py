# **kwargs collects all keyword arguments into a dictionary:

def show_info(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f" {key}: {value}")

show_info(name = "Alice", age = 32, city = "New York")

# Real World use - building profiles:

def create_profile(**kwargs):
    """Create a user profile from keyword arguments."""
    print("\n── USER PROFILE ──")
    for key, value in kwargs.items():
        print(f"{key.title()}: {value}")
    print("─────────────────")
create_profile(name = "Alice",
               age = 32,
               city = "New York",
               course = "Computer Science",
               goal = "CS Expert"
               )

# Accessing specific kwargs:

def introduce(**kwargs):
    name = kwargs.get("name", "Unknown")
    age = kwargs.get("age", 0)
    print(f"Hi, I'm {name}, and I'm {age} years old.")
    
introduce(name = "Alice", age = 32)
introduce(name = "Bob")
introduce()



