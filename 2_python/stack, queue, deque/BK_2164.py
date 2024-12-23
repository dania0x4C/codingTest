import sys
from collections import deque

N = int(sys.stdin.readline())
cards = deque()

for i in range(N):
    cards.append(i+1)

for _ in range(N-1):
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])
 
# pop() �ð� ���⵵�� O(n)�̴�
# deque()
