    # 1. Write a function 'make_adder(n)'
#    that returns a function which adds n to any number
#    add5 = make_adder(5)
#    add5(10) → 15
#    add5(3)  → 8
def make_adder(n):
	def adder(x):
		return x + n
	return adder
add5 = make_adder(5)
print(add5(15))
print(add5(8))

# 2. Write a counter using nonlocal:
#    def make_counter():
#        → returns a function that increments and returns count
#    counter = make_counter()
#    counter() → 1
#    counter() → 2
#    counter() → 3
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
counter = make_counter()
print(counter())
print(counter())
print(counter())