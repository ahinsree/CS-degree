# Local variable - exists only inside the function



def greet():
    message = "Hello, World!"  # This is a local variable
    print(message)

greet()

# Each function has its own scope
def function_a():
    x = 10 # x belongs to function_a only
    print(f"A: x = {x}")

def function_b():
    x =99 # x belongs to function_b only
    print(f"B: x = {x}")

function_a()             # A: x = 10
function_b()             # B: x = 99
# These two x variables NEVER interfere with each other

# Why local scope matters:
# 1. Avoids naming conflicts: You can use the same variable name in different functions
# 2. Encapsulation: Keeps data hidden inside functions, preventing accidental changes
# 3. Memory management: Local variables are created when the function is called and destroyed when the function exits, freeing up memory.
def calculate_tax(price):
    rate = 0.18  # rate is a local variable, only exists inside calculate_tax
    return price * rate

def calculate_discount(price):
    rate = 0.10  # rate is a different local variable, only exists inside calculate_discount
    return price * rate

# Both use 'rate' but they don't interfere ✅
print(calculate_tax(1000))       # 180.0
print(calculate_discount(1000))  # 100.0
 