import sys

T = int(sys.stdin.readline())

def factorial (a):
    result = 1

    for i in range(a):
        if (a != 0):
            result *= i+1
        else:
            result = 0
    return result

def combination(N, K):

    result = factorial(N) / (factorial(N-K) * factorial(K))

    return result

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(int(combination(M,N)))


