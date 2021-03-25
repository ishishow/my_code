import sys
args = sys.argv[1:]

if len(args) > 10:
    print("Error please under ten args")
    sys.exit()

person_A_time = 0
person_B_time = 0

for time in args[::-1]:
    if person_A_time <= person_B_time:
        person_A_time += int(time)
    else:
        person_B_time += int(time)

print(max(person_A_time,person_B_time))

