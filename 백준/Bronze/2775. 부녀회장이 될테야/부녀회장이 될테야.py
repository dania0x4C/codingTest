import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    K = int(sys.stdin.readline().strip())
    N = int(sys.stdin.readline().strip())

    # DP 테이블 초기화
    dp = [[0] * (N + 1) for _ in range(K + 1)]

    # 0층 초기화: i호에는 i명이 산다.
    for i in range(1, N + 1):
        dp[0][i] = i  

    # DP 채우기 (중복 계산 유지)
    for k in range(1, K + 1):  # 1층부터 K층까지
        for n in range(1, N + 1):  # 1호부터 N호까지
            person = 0  # 🔥 매번 초기화
            for h in range(1, n + 1):  # 1호부터 n호까지 합산 (중복 계산 유지)
                person += dp[k - 1][h]
            dp[k][n] = person  # 현재 층의 해당 호실 값 저장

    print(dp[K][N])
