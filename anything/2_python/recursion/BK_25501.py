import sys

N = int(sys.stdin.readline())



def recursion(s, l, r):
    global sum
    sum+=1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: 
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)
    
for _ in range(N):
    sum = 0
    word = sys.stdin.readline().rstrip()
    print(isPalindrome(word), sum)
        
# global ����

# �Լ� �ܺ��� ���� 
# ���� �� ��� o
# ���� �� ���� x

# �Լ� ������ ����
# ���� �� ��� o
# ���� �� ���� o

