import sys
args = sys.argv[1:]
count = int(args[0])
target_len = len(args[1])

if count < target_len:
    print(0)
else:
    print(2 ** (count - target_len + 1))
