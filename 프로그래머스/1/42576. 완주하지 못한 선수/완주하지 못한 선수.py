def solution(participant, completion):
    success = dict()
    for name in completion:
        if name in success:
            success[name] += 1
        else:
            success[name] = 1
            
    for name in participant:
        if name in success:
            success[name] -= 1
        else:
            return name
    
    for i in success:
        if success[i] == -1:
            answer = i
            
        
    return answer