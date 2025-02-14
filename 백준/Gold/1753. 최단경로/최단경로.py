import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

def dijkstra(start):
    dist = [INF] * (V + 1)  # 최단 거리 배열 (1-based index)
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))  # (거리, 노드)

    while pq:
        current_dist, node = heapq.heappop(pq)

        # 이미 처리된 노드라면 무시
        if current_dist > dist[node]:
            continue
        
        # 인접 노드 탐색
        for adj, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist[adj]:  # 더 짧은 경로 발견 시 갱신
                dist[adj] = new_dist
                heapq.heappush(pq, (new_dist, adj))

    return dist

# 입력 처리
V, E = map(int, input().split())  # 정점 개수, 간선 개수
startV = int(input().strip())  # 시작 정점

# 그래프 초기화 (1-based index)
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  # 단방향 그래프

# 다익스트라 실행
result = dijkstra(startV)

# 결과 출력
for i in range(1, V + 1):
    print(result[i] if result[i] != INF else "INF")
