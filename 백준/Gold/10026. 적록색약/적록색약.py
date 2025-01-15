import sys
from collections import deque

# 입력 처리
N = int(sys.stdin.readline().strip())
RGB = [list(sys.stdin.readline().strip()) for _ in range(N)]
visited_RG = [[False] * len(RGB[0]) for _ in range(N)]  # R/G를 같은 영역으로 처리할 때의 방문 체크
visited_R = [[False] * len(RGB[0]) for _ in range(N)]   # R의 독립 영역 체크
visited_G = [[False] * len(RGB[0]) for _ in range(N)]   # G의 독립 영역 체크
visited_B = [[False] * len(RGB[0]) for _ in range(N)]   # B의 독립 영역 체크


def bfs(start, RGB, visited, N, colors):
    """BFS 탐색: 지정된 색상 그룹(colors)에 해당하는 영역을 탐색"""
    queue = deque([start])
    visited[start[0]][start[1]] = True  # 시작 지점 방문 처리

    while queue:
        x, y = queue.popleft()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 상하좌우 이동

        for dx, dy in directions:
            nx, ny = x + dx, y + dy  # 다음 좌표 계산

            # 유효 범위 내, 방문하지 않음, 색상이 조건(colors)과 일치하는 경우
            if 0 <= nx < N and 0 <= ny < len(RGB[0]) and not visited[nx][ny]:
                if RGB[nx][ny] in colors:
                    visited[nx][ny] = True
                    queue.append((nx, ny))  # 큐에 다음 좌표 추가


# 영역 카운트
count_RG = 0  # R과 G를 같은 영역으로 처리한 경우
count_R = 0   # R만의 영역
count_G = 0   # G만의 영역
count_B = 0   # B만의 영역

# 탐색 (R/G를 같은 영역으로 처리한 경우)
for i in range(N):
    for j in range(len(RGB[0])):
        if not visited_RG[i][j]:
            if RGB[i][j] in ['R', 'G']:
                bfs((i, j), RGB, visited_RG, N, ['R', 'G'])
                count_RG += 1

# 탐색 (B를 독립적으로 처리한 경우)
for i in range(N):
    for j in range(len(RGB[0])):
        if not visited_B[i][j] and RGB[i][j] == 'B':  # B 영역 탐색
            bfs((i, j), RGB, visited_B, N, ['B'])
            count_B += 1

# 탐색 (R, G를 각각 따로 볼 때)
for i in range(N):
    for j in range(len(RGB[0])):
        if not visited_R[i][j] and RGB[i][j] == 'R':  # R 영역 탐색
            bfs((i, j), RGB, visited_R, N, ['R'])
            count_R += 1
        if not visited_G[i][j] and RGB[i][j] == 'G':  # G 영역 탐색
            bfs((i, j), RGB, visited_G, N, ['G'])
            count_G += 1


print(count_R + count_G + count_B)
print(count_RG + count_B)