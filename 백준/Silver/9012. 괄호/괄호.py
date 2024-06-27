import sys

T = int(sys.stdin.readline())

point = 0

result = list()
for _ in range(T):
    vps = sys.stdin.readline().strip()
    for i in vps:
        if(point >= 0) :
            if(i == ")"):
                point -= 1
            else:
                point += 1

    if(point == 0 ):
        result.append('YES')
    else:
        result.append("NO")
        point = 0

for i in result:
    print(i)
