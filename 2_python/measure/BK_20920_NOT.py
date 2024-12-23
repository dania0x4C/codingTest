import sys

N, M = map(int, sys.stdin.readline().split())
words = set()
check = dict()
length = 0
for _ in range(N):
    word = sys.stdin.readline().strip()
    if(len(word) >= M):
        if(length< len(word)):
            length = len(word)
sorted(word, key = lambda x: x[0])

## dict 정렬 알아보고 풀면 금방 풀 수 있음