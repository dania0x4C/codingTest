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
        
# global 변수

# 함수 외부의 선언 
# 변수 값 사용 o
# 변수 값 변경 x

# 함수 내부의 선언
# 변수 값 사용 o
# 변수 값 변경 o

