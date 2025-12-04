import sys

expression = input().strip().split('-')
result = 0
mCounter = 0
for e in expression:
    if mCounter == 0:
        chunk = list[int]((map(int, e.split('+'))))
        for c in chunk:
            result += int(c)
    else:
        chunk = list((map(int, e.split('+'))))
        for c in chunk:
            result -= int(c)

    mCounter += 1

print(result)