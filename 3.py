stack = 0
for i in range(50000):
    if i % 3 == 0 or "3" in str(i):
        # print i
        stack += i

print stack
