import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
result = list()
circle = deque()

for i in range(N):
    circle.append(i+1)

for _ in range(N):
    circle.rotate(-(K-1))
    result.append(circle.popleft())
    
print("<" + ", ".join(map(str, result)) + ">")

# print(", ".join)