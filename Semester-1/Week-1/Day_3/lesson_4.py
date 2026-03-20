# break → stop the loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)
# continue → skip this iteration   
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# pass → placeholder, does nothing    
for i in range(5):
    if i ==3:
        pass
    print(i)
    