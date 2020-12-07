# a * b / 2 < 8192

# a ** 2 + b ** 2
import math
stack = 0
a = 1
b = 1
while  a * b / 2 <= 8192:
    while a * b / 2 <= 8192:
        if math.sqrt(a ** 2 + b ** 2) % 1 == 0:
            stack += 1
        a += 1
    print a
    print b
    b += 1
    a = b
print stack
