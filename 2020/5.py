# 1000000
result = 0
for i in range(100):
    stack = 1
    for j in range(3):
        # print i
        for k in range(len(str(i))):
            print int(str(i)[k])
            stack *= int(str(i)[k])
        print stack, j
        if stack == 0 or stack / 10 == 0:
            print "j="
            print j
            if j == 2:
                result += 1
            break
        elif j > 2:
            break

print result
