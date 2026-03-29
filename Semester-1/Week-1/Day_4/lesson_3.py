'''pass — the placeholder:'''
# pass does absolutely nothing
# Python just moves to the next line

for i in range(1, 6):
    if i == 3:
        pass             # todo: add logic here later
    print(i, sep=' ', end=' ')
print()
# pass had ZERO effect on the output
'''When is pass actually useful?'''
score = 70
# 1. When planning code structure before writing it
if score >= 90:
    pass  # Will add grade logic later
elif score >= 80:
    pass  # Will add grade logic later
# 2. Empty function you plan to fill in later
def calculate_tax():
    pass               # coming soon!
# 3. Empty class definition
class BankAccount:
    pass               # will build this in Week 11 OOP
'''else on loops — Python's unique feature:'''
# else runs ONLY if the loop finished
# WITHOUT hitting a break

# Example 1 — else runs (no break hit)
for i in range(1, 6):
    print(i, sep=' ', end=' ')
else:
    print("\nLoop completed normally, no break hit.✅")
# Example 2 — else does NOT run (break hit)
for i in range(1, 6):
    if i == 3:
        break
    print(i, sep=' ', end=' ')
    print()
else:
    print("This will not print because break was hit.❌")
#         (else skipped because break was hit)     
'''Real-world — prime number checker:'''
num = 17
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is NOT prime ❌")
        break
else:
    print(f"{num} is prime ✅", sep=' ', end='\n')