import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())

que = deque()

for i in range(N):
    que.append(i+1)

print("<", end ="")

for _ in range(N):
    que.rotate(-K+1)
    print(que.popleft(), end ="")
    if len(que):
        print(", ", end="")
print(">")