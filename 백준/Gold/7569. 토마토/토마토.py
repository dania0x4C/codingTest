import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().strip().split())
visited = [[[False] * M for _ in range(N)] for _ in range(H)]
box = [[list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)] for _ in range(H)]
cooked = deque()
cook_day = -1
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:
                cooked.append((h, n, m))
                visited[h][n][m] = True

def bfs():
    direction = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    global cook_day
    while cooked:
        cook_day +=1
        for _ in range(len(cooked)):
            h, n, m = cooked.popleft()

            for dh, dn, dm in direction:
                ch, cn, cm = dh + h, dn + n, dm + m

                if 0 <= ch < H and 0 <= cm < M and 0 <= cn < N and visited[ch][cn][cm] == False:
                    visited[ch][cn][cm] = True
                    
                    if box[ch][cn][cm] == 0:
                        cooked.append((ch, cn, cm))
                    
                    box[ch][cn][cm] = 1

bfs()

all_tomato = True

for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0:
                all_tomato = False

if all_tomato:
    print(cook_day)
else:
    print(-1)