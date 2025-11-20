import sys

s = input()
count = 0
minb = 100000

ss = s + s

for c in s:
    if c == 'a':
        count += 1

for i in range(len(s)):
    countb = 0

    for j in range(i, count + i):
        if ss[j] == 'b':
            countb += 1
    minb = min(countb, minb)

print(minb)
