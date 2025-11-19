import sys
from collections import deque

computerNum = int(input())
computersV = int(input())

network = [[] for _ in range(computerNum + 1)]

for _ in range(computersV):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

visited = [False] * (computerNum + 1)
visited[1] = True
q = deque([1])

def bfs():
    count = 0
    while q:
        current = q.popleft()

        for next in network[current]:
            if visited[next] == False:
                visited[next] = True
                q.append(next)
                count+=1
    return count

print(bfs())
