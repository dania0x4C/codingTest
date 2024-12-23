import sys

N = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))

print(max(number)*min(number))

## 하나의 수에서 약수를 생각하면 약수보다 작지만 가장 큰 수는 원래의 수에서 가장 작은 약수를 나눈 수 이다 그렇기 때문에 가장 큰 값에 가장 작은 값을 곱하면 수가 나온다.