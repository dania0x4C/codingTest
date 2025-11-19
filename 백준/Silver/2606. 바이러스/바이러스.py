import sys
from collections import deque

computerNum = int(input())
computersV = int(input())
network = [list(map(int, input().strip().split())) for _ in range(computersV)]
visited = [False] * (computerNum + 1)
visited[1] = True
q = deque([1])
def bfs(network, visited):
    count = 0
    while q:
        select = q.popleft()

        for s, e in network:
            if select == s and visited[e] == False:
                visited[e] = True
                q.append(e)
                count += 1
            elif select == e and visited[s] == False:
                visited[s] = True
                q.append(s)
                count += 1

    return count

print(bfs(network, visited))
