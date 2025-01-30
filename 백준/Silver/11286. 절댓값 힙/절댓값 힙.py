import heapq
import sys

input = sys.stdin.readline
N = int(input().strip())

heap = []

def heapPush(x):
    # 절댓값 기준 정렬을 위해 (절댓값, 실제값) 저장
    heapq.heappush(heap, (x if x >= 0 else -x, x))

def heapPop():
    if heap:
        # 최소값 pop
        _, value = heapq.heappop(heap)
        print(value)
    else:
        # 힙이 비어 있는 경우
        print(0)

# 입력 처리
for _ in range(N):
    x = int(input().strip())
    if x != 0:
        heapPush(x)
    else:
        heapPop()
