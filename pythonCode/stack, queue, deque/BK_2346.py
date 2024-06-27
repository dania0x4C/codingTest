import sys
from collections import deque

N = int(sys.stdin.readline())
index = deque()
balloon = deque(sys.stdin.readline().split())

for i in range(N):
    index.append(i+1)
result = list()

for _ in range(N):

    value = balloon.popleft()
    key = index.popleft()
    balloon.rotate(-int(value))
    index.rotate(-int(value))
    result.append(key)

for i in result:
    print(i)

