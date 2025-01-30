import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
trees = list(map(int, data[2:]))

low, high = 0, max(trees)  # 가능한 cutLine의 범위 설정

def get_wood(cut):
    return sum(max(0, tree - cut) for tree in trees)

while low <= high:
    mid = (low + high) // 2
    wood = get_wood(mid)
    if wood < M:
        high = mid - 1
    else:
        low = mid + 1

# 이분 탐색을 완료한 후, high는 조건을 만족하는 최대 cutLine
print(high)
