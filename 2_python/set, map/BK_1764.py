import sys

n, m = map(int, sys.stdin.readline().split())
nameH = set()
nameHS = set()
for _ in range(n):
    nameH.add(sys.stdin.readline().strip())

for _ in range(m):
    nameS = sys.stdin.readline().strip()
    if nameS in nameH:
        nameHS.add(nameS)

nameHS = sorted(nameHS)

print(len(nameHS))

for i in nameHS:
    print(i)


# import sys

# n, m = map(int, sys.stdin.readline().split())
# nameH = list()
# nameHS = list()
# for _ in range(n):
#     nameH.append(sys.stdin.readline().strip())

# for _ in range(m):
#     nameS = sys.stdin.readline().strip()
#     if nameS in nameH:
#         nameHS.append(nameS)

# nameHS = sorted(nameHS)

# print(len(nameHS))

# for i in nameHS:
#     print(i)
    
#list를 사용할때 for{append}는 n * n 의 시간 복잡도를 가진다