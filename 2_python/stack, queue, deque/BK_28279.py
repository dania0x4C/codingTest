import sys
from collections import deque

N = int(sys.stdin.readline())
result = deque()
show = list()

for _ in range(N):
    select = sys.stdin.readline().split()
    if select
    == "1":
        result.appendleft(select[1])

    elif select[0] == "2":
        result.append(select[1])

    elif select[0] == "3":
        if(len(result) == 0):
            show.append("-1")
        else:
            show.append(result.popleft())

    elif select[0] == "4":
        if(len(result) == 0):
            show.append("-1")
        else:
            show.append(result.pop())

    elif select[0] == "5":
        show.append(len(result))

    elif select[0] == "6":
        if(len(result)==0):
            show.append(1)
        else:
            show.append(0)

    elif select[0] == "7":
        if(len(result)==0):
            show.append("-1")
        else:
            show.append(result[0])
    elif select[0] == "8":
        if(len(result)==0):
            show.append("-1")
        else:
            show.append(result[len(result)-1])

for i in show:
    print(i)
