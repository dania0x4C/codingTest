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
# pop: list.pop(indexNum) �ش� index�� �����ϴ� �� ����, �Է� �� �ϴ� ��� �� ������ ��� ����(stack)

# remove: list.remove(value) �ش� value�� list�� �����ϸ� ���� ����

# clear: list.clear() ��� ��Ҹ� ����

# del: del list[indexNum] �ش� index�� ���� ����