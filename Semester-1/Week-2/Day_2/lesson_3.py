# The LEGB rule in Python stands for Local, Enclosing, Global, and Built-in. It is the order in which Python looks for variables when they are referenced in a function or a block of code.

"""L → Local      (inside current function)
   E → Enclosing  (inside outer function, if nested)
   G → Global     (module level — top of file)
   B → Built-in   (Python's built-in names like print, len, range)"""
   
# Built-in scope - B

print("Hello") # "print" is a built-in function, so it is in the built-in scope.
len("Hello") # "len" is also a built-in function, so it is in the built-in scope.

# Global scope - G
x = "Global x" # "x" is defined at the module level, so it is in the global scope.
def outer():
    # Enclosing scope - E
    x = "enclosing x"
    def inner():
        #Local scope - L
        x = "local x"
        print(x)    # finds x in LOCAL first -> "local x"
    inner()
    print(x)       # finds x in ENCLOSING -> "enclosing x"
outer()
print(x)           # finds x in GLOBAL -> "global x"

# LEGB in action — step by step:

name = "Global Ahinsree"      # G

def outer():
    name = "Enclosing Ahinsree"   # E

    def inner():
        name = "Local Ahinsree"   # L
        print(name)   # L wins → "Local Ahinsree"

    inner()
    print(name)       # E wins → "Enclosing Ahinsree"

outer()
print(name)           # G wins → "Global Ahinsree"

# What happens when a name is NOT found locally:

total = 100      # G

def show():
    # no local 'total defined
    print(total)              #Python searches  L->E->G-> finds it it G ✅
    
show()
