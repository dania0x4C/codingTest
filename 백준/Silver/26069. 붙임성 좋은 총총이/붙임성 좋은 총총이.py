import sys

N = int(sys.stdin.readline().strip())
dance = set()
dance.add("ChongChong")

for _ in range(N):
    name1, name2 = map(str,sys.stdin.readline().split())

    if name1 in dance:
        dance.add(name2)
    elif name2 in dance:
        dance.add(name1)
    
print(len(dance))
# set에 넣고  for in  으로 확인 그리고 마지막에 있으면 새로원 사람 추가