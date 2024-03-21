import sys

k = int(sys.stdin.readline())
book = list()
result = 0
for _ in range(k):
    number = int(sys.stdin.readline())
    if(number == 0):
        book.pop()
    else:
        book.append(number)

for i in book:
    result += i

print(result)
# pop: list.pop(indexNum) 해당 index에 존재하는 값 삭제, 입력 안 하는 경우 맨 마지막 요소 삭제(stack)

# remove: list.remove(value) 해당 value가 list에 존재하면 값을 삭제

# clear: list.clear() 모든 요소를 삭제

# del: del list[indexNum] 해당 index의 값을 삭제