#/bin/env python3

increase = 0
previous = None
data = list(map(int, open("input.txt")))

for i, entry in enumerate(data):
    if i < 2:
        continue
    
    # Sum current value + previous two values
    slide = entry + data[i-1] + data[i-2]
    # ++ if greater than previous sum
    if previous is not None and slide > previous:
        increase += 1

    previous = slide

print(f"The answer is {increase}")