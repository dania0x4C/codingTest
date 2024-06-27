import sys

N, K = map(int, sys.stdin.readline().split())

def factorial (a):
    result = 1

    for i in range(a):
        if (a != 0):
            result *= i+1
        else:
            result = 0
    return result

result = factorial(N) / (factorial(N-K) * factorial(K))

print(int(result))