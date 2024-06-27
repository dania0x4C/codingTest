import sys

N = int(sys.stdin.readline())
result = 1

for i in range(N):
    if (N != 0):
        result *= i+1
    else:
        result = 0
    
print(result)