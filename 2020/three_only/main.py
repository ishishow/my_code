def except_three(num):
    stack = 0
    for i in range(num):
        if i % 3 == 0 or "3" in str(i):
            # print(i)
            stack += i
    return stack


if __name__ == '__main__':
    print(except_three(10))




