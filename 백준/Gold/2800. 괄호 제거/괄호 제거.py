import sys
from itertools import combinations

# 여는 괄호와 닫는 괄호 인덱스를 저장할 리스트
parentheses_pairs = []

# 입력 문자열
Input = sys.stdin.readline().strip()
# Input = '(1+(2*(3+4)))'

# 괄호 인덱스 수집
stack = []
for i, char in enumerate(Input):
    if char == '(':
        stack.append(i)  # 여는 괄호 인덱스 스택에 추가
    elif char == ')':
        if stack:
            open_index = stack.pop()  # 가장 최근 여는 괄호 인덱스와 짝을 이룸
            parentheses_pairs.append((open_index, i))

ParenthesesLen = len(parentheses_pairs)

# 모든 결과 문자열을 저장할 집합
results = set()

for i in range(1, ParenthesesLen + 1):  # 최소 하나의 괄호 제거부터 시작
    outputParentheses = combinations(parentheses_pairs, i)

    for j in outputParentheses:  # 괄호 인덱스 조합
        # 제거할 인덱스 수집
        remove_indices = set()
        for open_index, close_index in j:
            remove_indices.add(open_index)
            remove_indices.add(close_index)

        # 새로운 문자열 생성
        new_string = ''.join(
            Input[k] for k in range(len(Input)) if k not in remove_indices
        )

        # 결과를 집합에 추가
        results.add(new_string)

# 결과를 정렬하여 출력
for result in sorted(results):
    print(result)