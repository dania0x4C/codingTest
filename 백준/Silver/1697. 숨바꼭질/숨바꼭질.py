import sys
from collections import deque

N, K = map(int, input().split())

# 문제의 최대 범위는 100,000입니다.
MAX = 100000
visited = [0] * (MAX + 1) # 0 ~ 100,000번 인덱스 생성

queue = deque([N])

while queue:
    x = queue.popleft()

    if x == K:
        print(visited[x])
        break

    for next_x in (x-1, x+1, x*2):
        # 수정 1: 0번 인덱스도 포함해야 하므로 0 <= next_x
        # 수정 2: 최대 범위는 MAX(100,000)까지만 허용
        if 0 <= next_x <= MAX and visited[next_x] == 0:
            visited[next_x] = visited[x] + 1
            queue.append(next_x)