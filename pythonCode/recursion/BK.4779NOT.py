import sys

N = int(sys.stdin.readline().rstrip())
N3 = 3**N
S ="-" * N3

def PrintStar():
    for i in range(N):
        for j in range(N):
            print("*")
      print("/n")