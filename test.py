import sys
from collections import deque

jumpEnergy = deque()

N = int(sys.stdin.readline().strip())

for i in range(N-1):
    smallJump, bigJump = map(int, sys.stdin.readline().strip().split())
    jumpEnergy.append({'smallJump': smallJump, 'bigJump': bigJump})

K = int(sys.stdin.readline().strip())

checkStone = 0
useEnergy = 0

def chooseJump(i, checkStone, N, jumpEnergy, K):
    if N-2 == checkStone:
        return 1, jumpEnergy[i]['smallJump']

    # 범위 검사
    next1_small = jumpEnergy[i+1]['smallJump']
    next2_small = jumpEnergy[i+2]['smallJump']

    current_small = jumpEnergy[i]['smallJump']
    current_big = jumpEnergy[i]['bigJump']

    if current_small + next1_small + next2_small < K or current_small + next1_small < K:
        if current_small + next1_small < current_big:
            return 1, current_small
        else:
            return 2, current_big
    else:
        return 3, K

i = 0
while N-1 > checkStone:
    jump, energy = chooseJump(i, checkStone, N, jumpEnergy, K)
    checkStone += jump
    useEnergy += energy
    i += 1

print(useEnergy)
