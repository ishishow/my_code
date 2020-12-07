def tribonacci_list(n, t0, t1, t2):
    tri = [t0, t1, t2]
    if n == 1:
        tri = [t0]
    elif n == 2:
        tri = [t0, t1]
    else:
        for k in range(3, n):
            tri.append(tri[k - 1] + tri[k - 2] + tri[k - 3])
    return tri


tri = tribonacci_list(28, 1, 0, 5)

print(tri)
