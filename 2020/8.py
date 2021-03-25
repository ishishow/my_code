import sys

args = sys.argv
if len(args) != 3:
    print("Error please input two args")
    sys.exit()

first = args[1]
second = args[2]
ans = ""

for x in range(1, len(first)):
    if first[len(first)-x] == second[len(second)-x]:
        ans += first[len(first)-x]

if ans != "":
    print(ans[::-1])

