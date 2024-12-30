import sys

pipe = sys.stdin.readline().strip()

pipeCount = 0
pipeCut = 0

for i in range(len(pipe)):

    if pipe[i] == "(":                                                                                                                                                                                                                                                                                                        
        pipeCount += 1
    else:
        pipeCount -= 1
        if pipe[i-1] == "(":
            pipeCut += pipeCount
        else:
            pipeCut += 1

print(pipeCut)