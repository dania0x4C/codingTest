import sys
from collections import deque

# 나이트의 8가지 이동 방향
directions = [(1, 2), (2, 1), (-1, 2), (-2, 1),
              (-2, -1), (-1, -2), (1, -2), (2, -1)]

def bfs(l, start, target):
    visited = [[False] * l for _ in range(l)]
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True

    count = 0  # 이동 횟수

    while queue:
        for _ in range(len(queue)):  # 현재 레벨의 모든 노드 탐색
            x, y = queue.popleft()

            if (x, y) == target:     # 목표 지점 도착
                return count

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # 체스판 범위 내 & 방문하지 않은 곳
                if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

        count += 1  # 현재 레벨 탐색 완료 후 이동 횟수 증가

# 테스트 케이스 입력
TC = int(sys.stdin.readline().strip())
for _ in range(TC):
    l = int(sys.stdin.readline().strip())                        # 체스판 크기
    current = tuple(map(int, sys.stdin.readline().split()))     # 시작 위치
    target = tuple(map(int, sys.stdin.readline().split()))      # 목표 위치

    # 결과 출력
    print(bfs(l, current, target))
