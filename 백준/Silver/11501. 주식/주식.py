import sys

T = int(input())
for _ in range(T):
    N = int(input())
    points = list(map(int, input().strip().split()))
    value = 0
    max_point = 0

    for i in range(len(points) - 1, -1, -1):
        max_point = max(points[i], max_point)

        if points[i]< max_point:
            value += max_point - points[i]
    print(value)
    