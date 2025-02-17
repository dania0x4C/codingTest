import sys

T = int(sys.stdin.readline().strip())
for i in range(T):
    N = int(sys.stdin.readline().strip())
    dp = [0] * N
    if N < 3:
        print(1)
        continue

    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    for i in range(3,N):
        dp[i] = dp[i-2] + dp[i-3]

    print(dp[N-1])