import sys

# 입력 받기
N = int(sys.stdin.readline().strip())
T = []
P = []
dp = [0] * (N + 1)  # dp[i] → i번째 날까지 얻을 수 있는 최대 수익

for _ in range(N):
    i, j = map(int, sys.stdin.readline().split())
    T.append(i)
    P.append(j)

# DP 적용 (뒤에서부터 거꾸로 계산)
for i in range(N - 1, -1, -1):
    if i + T[i] <= N:  # 상담을 할 수 있는 경우
        dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]])
    else:  # 상담을 할 수 없는 경우 (넘어감)
        dp[i] = dp[i + 1]

# 최대 수익 출력
print(dp[0])
