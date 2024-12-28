import sys
from collections import deque
X = sys.stdin.readline()

que = deque()
def push(que, req):
    que.appendleft(req)

def pop(que):
    if(len(que) == 0):
        print(-1)
    else:
        popFirst = que.popleft()
        print(popFirst)

def size(que):
    queLength = len(que)
    print(queLength)

def empty(que):
    if(len(que) == 0):
        print(1)
    else:
        print(0)

def top(que):
    if(len(que) == 0):
        print(-1)
    else:
        print(que[0])


        

for _ in range(int(X)):
    command= sys.stdin.readline().strip().split()
    a = command[0]
    b = command[1] if len(command) > 1 else None
    if(a == "push"):
        push(que, int(b))
    if(a == "top"):
        top(que)
    if(a == "empty"):
        empty(que)
    if(a == "size"):
        size(que)
    if(a == "pop"):    
        pop(que)