import sys

N, M = map(int, sys.stdin.readline().split())
# N = 4
# M = 2
result = []

def backTracking(depth):
    
    if depth == M:
        for i in result:
            print(i, end = " ")
        print()

    for i in range(1, N+1):
        if i not in result :
            result.append(i)
            backTracking(depth+1)
            result.pop()

backTracking(0)