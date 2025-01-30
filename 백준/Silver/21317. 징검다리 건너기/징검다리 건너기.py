import sys
input = sys.stdin.read

data = input().split()

N = int(data[0])
index = 1
jumpEnergy = []
for i in range(N-1):
    smallJump, bigJump = map(int, data[index:index+2])
    jumpEnergy.append((smallJump, bigJump))
    index += 2

K = int(data[index])

# DP 테이블 초기화
dp_no_super = [float('inf')] * N  # 슈퍼 점프를 사용하지 않았을 때
dp_super_used = [float('inf')] * N  # 슈퍼 점프를 사용했을 때

dp_no_super[0] = 0  # 시작 지점

for i in range(N-1):
    # 슈퍼 점프를 사용하지 않은 상태 업데이트
    if i + 1 < N:
        dp_no_super[i+1] = min(dp_no_super[i+1], dp_no_super[i] + jumpEnergy[i][0])
    if i + 2 < N:
        dp_no_super[i+2] = min(dp_no_super[i+2], dp_no_super[i] + jumpEnergy[i][1])
    
    # 슈퍼 점프를 사용한 상태 업데이트
    # 슈퍼 점프를 이번에 처음 사용하는 경우
    if i + 3 < N:
        dp_super_used[i+3] = min(dp_super_used[i+3], dp_no_super[i] + K)
    
    # 이미 슈퍼 점프를 사용한 상태에서의 계속 업데이트
    if i + 1 < N:
        dp_super_used[i+1] = min(dp_super_used[i+1], dp_super_used[i] + jumpEnergy[i][0])
    if i + 2 < N:
        dp_super_used[i+2] = min(dp_super_used[i+2], dp_super_used[i] + jumpEnergy[i][1])

# 결과 출력: N-1번째 돌에 도착하는 최소 에너지
result = min(dp_no_super[N-1], dp_super_used[N-1])
print(result)
