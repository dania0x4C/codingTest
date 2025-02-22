import sys

N, K = map(int, sys.stdin.readline().strip().split())
coins = [int(sys.stdin.readline().strip()) for _ in range(N)]

dp = [0] * (K + 1)
dp[0] = 1  # 0원을 만드는 경우는 '아무 동전도 사용하지 않는 경우' 단 하나

for coin in coins:  # 각 동전에 대해
    for k in range(coin, K + 1):  # 해당 동전부터 시작해서 K까지 경우의 수를 누적
        dp[k] += dp[k - coin]

print(dp[K])
