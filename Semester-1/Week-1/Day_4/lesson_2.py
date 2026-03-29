''' continue skips the rest of the current iteration and jumps straight to the next one.
The loop keeps going — only that one cycle is skipped.'''
# Basic continue
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, sep=' ', end=' ')
print()

# Real-World __ skip invalid data__
scores = [85, -5, 92, -1, 78, 101, 65]
print("Valid scores:", end=' ')
for score in scores:
    if score < 0 or score > 100:
        continue 
    print(score, sep=' ', end=' ')
print()
# break vs continue — side by side:
# continue → skips ONE cycle, loop keeps going
for i in range(1, 6):
    if i == 3:
        continue
    print(i, sep=' ', end=' ')
print()
# break → stops the ENTIRE loop
for i in range(1, 6):
    if i == 3:
        break
    print(i, sep=' ', end=' ')
print()
   