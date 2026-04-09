# Task 1: What does this print? Explain WHY:
x = 10
def change():
    x = 99
    print(f"Inside: {x}")
change()
print(f"Outside: {x}")

# Task 2: What happens here? Fix it:
total = 0
def add(n):
    global total
    total += n
    return total
print(add(10))
print(add(20))
print(add(30)) 

# Task 3: Predict the output — trace through LEGB:

name = "Global"
def outer():
    name = "Enclosing"
    def inner():
        name = "Local"
        print(name)
    inner()
    print(name)
outer()
print(name)