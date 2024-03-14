import sys

n = int(sys.stdin.readline())
check = dict()

for _ in range(n):
    name, log = map(str, sys.stdin.readline().split())
    check[name] = log
    if (log == "leave"):
        check.pop(name)

check = sorted(check, reverse=True)
for i in check:
    print(i)
