#/bin/env python3

increase = 0
previous = None

for line in open('input.txt'):
    print(line)
    if previous is not None and int(line) > previous:
        increase += 1
    previous = int(line)

print(f"The answer is {increase}")

