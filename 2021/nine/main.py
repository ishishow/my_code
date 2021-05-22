import sys


def main(argv):

    minMonsterLevel = int(argv[0])
    maxMonsterLevel = int(argv[1])
    magicKind = int(argv[2])
    magicNumArray = list(map(int, argv[3:]))
    if 1 in magicNumArray:
        print(0)
        return

    aa = []
    for i in range(len(magicNumArray)):
        for j in magicNumArray[i+1:]:
            aa.append(magicNumArray[i]*j)
    print(aa)

    answer = maxMonsterLevel - minMonsterLevel + 1
    print(answer)

    for i in magicNumArray:
        if (maxMonsterLevel-minMonsterLevel) > i:
            a = (maxMonsterLevel-minMonsterLevel) // i
            answer = answer - a - 1
    print(answer)

    for i in aa:
        print(i)
        if (maxMonsterLevel-minMonsterLevel) >= i:
            a = (maxMonsterLevel-minMonsterLevel) // i
            answer = answer + a + 1

    print(answer)


if __name__ == '__main__':
    main(sys.argv[1:])
