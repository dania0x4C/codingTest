import sys

# 표준 입력에서 데이터 읽기
N = int(sys.stdin.readline().strip())
numbers = [int(sys.stdin.readline().strip()) for _ in range(N)]

# 평균 계산
average = sum(numbers) / len(numbers)

# 평균이 -0.0이면 0.0으로 변환
if average == -0.0:
    average = 0.0

# 결과 출력
print(round(average))

# 추가 계산: 중앙값, 최빈값, 범위
sorted_numbers = sorted(numbers)
n = len(sorted_numbers)

# 중앙값 계산
if n % 2 == 1:
    median = sorted_numbers[n // 2]
else:
    median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

# 최빈값 계산
from collections import Counter
counter = Counter(numbers)
max_frequency = max(counter.values())
modes = [k for k, v in counter.items() if v == max_frequency]
modes.sort()

# 두 번째로 작은 최빈값 선택
mode_result = modes[1] if len(modes) > 1 else modes[0]

# 범위 계산
range_value = max(numbers) - min(numbers)

# 중앙값, 최빈값, 범위 출력
print(median)
print(mode_result)
print(range_value)
