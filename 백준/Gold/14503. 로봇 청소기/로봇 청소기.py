import sys

N, M = map(int, sys.stdin.readline().strip().split())

r, c, d = map(int, sys.stdin.readline().strip().split())

world = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
cleanCount = 0

def clean(r, c, d):
    global cleanCount
    # 1
    if world[r][c] == 0:
        world[r][c] = -1
        cleanCount += 1
    # 3
    if world[r][c+1] == 0 or world[r][c-1] == 0 or world[r+1][c] == 0 or world[r-1][c] == 0:
        # 3-1
        if d == 0:
            d = 3
        else:
            d -= 1
        # 3-2
        if d == 0 and world[r-1][c] == 0:
            return r-1, c, 0
        elif d == 1 and world[r][c+1] == 0:
            return r, c+1, 1
        elif d == 2 and world[r+1][c] == 0:
            return r+1, c, 2
        elif d == 3 and world[r][c-1] == 0:
            return r, c-1, 3
        else:
            return r, c, d
    # 2
    else:
        # 2-1, 2-2
        if d == 0:
            if world[r+1][c] == 1:
                return -1, -1, -1
            else:    
                return r+1, c, 0
        elif d == 1:
            if world[r][c-1] == 1:
                return -1, -1, -1
            else:
                return r, c-1, 1
        elif d == 2:
            if world[r-1][c] == 1:
                return -1, -1, -1
            else:
                return r-1, c, 2
        else:
            if world[r][c+1] == 1:
                return -1, -1, -1
            else:
                return r, c+1, 3

while 1:
    r, c, d = clean(r, c, d)
    if d == -1:
        print(cleanCount)
        break