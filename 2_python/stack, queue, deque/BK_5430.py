import sys
from collections import deque

# 백준 테스트용 - input.txt를 stdin으로 리다이렉트
sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

def D(dequeue, Rcount):
    if not dequeue:
        return False
    if Rcount % 2 == 0:
        dequeue.popleft()

    else:
        dequeue.pop()

    return True

T = int(input())
for _ in range(T):
    dequeue = deque()
    fucs = input()#.strip()
    n = int(input())
    array_str = input()#.strip()
    
    if array_str == "[]" or n == 0:
        # 빈 배열인 경우
        pass
    else:
        # '[' 와 ']' 제거하고 쉼표로 분리
        numbers = array_str[1:-1].split(',')
        for num in numbers:
            dequeue.append(int(num))

    error = False
    for fuc in fucs:
        Rcount = 0
        if fuc == 'D':
            if not D(dequeue, Rcount):
                error = True
                break
        elif fuc == 'R':
            Rcount += 1
    
    if error:
        print('error')
    else:
        # 결과를 배열 형태로 출력
        result = list(dequeue)
        print('[' + ','.join(map(str, result)) + ']')