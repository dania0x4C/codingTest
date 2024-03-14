import sys

n, m = map(int, sys.stdin.readline().split())
s = set()
sum=0
for _ in range(n):
    s.add(sys.stdin.readline().strip())

for _ in range(m):
    w = sys.stdin.readline().strip()
    if w in s:
        sum+=1

print(sum)

# python 집합
# a | b = a.union(b) = 합집합
# a & b = a.intersection(b) = 교집합
# a - b = a.difference(b) = 차집합
#
# python if문
# if a in (list, dic, 문자열 등등)
# 안에 있는지 확인 하는 방법이 존재