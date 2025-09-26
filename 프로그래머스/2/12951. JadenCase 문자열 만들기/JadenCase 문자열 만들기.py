def solution(s):
    pre = ' '
    result = ''
    for c in s:
        if pre == ' ':
            result += c.upper()
        else:
            result += c.lower()
        pre = c
            
    return result