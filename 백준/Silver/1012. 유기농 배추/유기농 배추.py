import sys
from collections import deque

input = sys.stdin.read
data = input().split()

idx = 0
T = int(data[idx])
idx += 1

def bfs(start, field, visited, M, N):
    queue = deque([start])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 방향 이동
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and field[ny][nx] == 1:
                visited[ny][nx] = True
                queue.append((ny, nx))

results = []
for _ in range(T):
    M = int(data[idx])
    N = int(data[idx + 1])
    K = int(data[idx + 2])
    idx += 3
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    count = 0

    for _ in range(K):
        X = int(data[idx])
        Y = int(data[idx + 1])
        idx += 2
        field[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                bfs((i, j), field, visited, M, N)
                count += 1

    results.append(count)

for result in results:
    print(result)
