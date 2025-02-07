import sys

N = int(sys.stdin.readline().strip())
plus_numbers = []
minus_numbers = []
zero = False
ones_count = 0
result = 0

# 입력 처리
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    if num > 1:
        plus_numbers.append(num)
    elif num == 1:
        ones_count += 1
    elif num == 0:
        zero = True
    else:
        minus_numbers.append(num)

# 양수는 큰 수부터 정렬 (내림차순)
plus_numbers.sort(reverse=True)

# 음수는 절댓값이 큰 순서로 정렬 (내림차순)
minus_numbers.sort()

# 1️⃣ 양수 처리
i = 0
while i < len(plus_numbers) - 1:
    result += plus_numbers[i] * plus_numbers[i+1]
    i += 2

# 남은 양수 처리
if i < len(plus_numbers):
    result += plus_numbers[i]

# 2️⃣ 음수 처리
i = 0
while i < len(minus_numbers) - 1:
    result += minus_numbers[i] * minus_numbers[i+1]
    i += 2

# 남은 음수 처리
if i < len(minus_numbers):
    if not zero:
        result += minus_numbers[i]

# 3️⃣ 1 처리
result += ones_count

# 결과 출력
print(result)
