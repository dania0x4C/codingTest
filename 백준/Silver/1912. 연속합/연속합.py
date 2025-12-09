import sys

n = int(input().strip())
sequence = list(map(int, input().strip().split()))

dp = [0] * n 
dp[0] = sequence[0]
for i in range(1, n):
    dp[i] = max(sequence[i] + dp[i-1], sequence[i])

print(max(dp))
