import sys

N = int(sys.stdin.readline().strip())

number = [0 for _ in range(10)]

for i in range(N):
    if i == 0:
        for j in range(9):
            number[j+1] = 1
    else:
        new_number = [0 for _ in range(10)]
        for j in range(len(number)):
            if j == 0:
                new_number[1] += number[0] 
            elif j == 9:
                new_number[8] += number[9]
            else:
                new_number[j-1] += number[j]
                new_number[j+1] += number[j]
        number = new_number

print(sum(number) % 1000000000)