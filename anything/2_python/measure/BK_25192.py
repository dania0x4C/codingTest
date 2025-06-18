import sys

N = int(sys.stdin.readline())
user = set()
result = 0
for _ in range(N):
    check = sys.stdin.readline().strip()
        
    if check == "ENTER":
        result += len(user)
        user.clear()
    else:
        if check not in user:
            user.add(check)
result += len(user)
print(result)

# if "value" in list: - 시간복잡도가 O(N) set = 시간복잡도 O(1)
 
# dictName[key] = value


