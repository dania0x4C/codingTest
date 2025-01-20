import sys

N = int(sys.stdin.readline().strip())

gameWord = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def count_paths(gameWord, N):
    # DP 테이블 초기화: 모든 값을 0으로 설정
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = 1  # 시작 위치

    for i in range(N):
        for j in range(N):
            if dp[i][j] == 0 or gameWord[i][j] == 0:
                continue  # 이동 불가능하거나 도달 불가능한 경우

            move = gameWord[i][j]
            # 수직 이동
            if i + move < N:
                dp[i + move][j] += dp[i][j]
            # 수평 이동
            if j + move < N:
                dp[i][j + move] += dp[i][j]

    return dp[N-1][N-1]

print(count_paths(gameWord, N) )