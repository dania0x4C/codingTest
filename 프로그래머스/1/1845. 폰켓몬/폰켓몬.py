def solution(nums):
    pocketmons = dict()
    for num in nums:
        
        if num in pocketmons:
            pocketmons[num] += 1
        else:
            pocketmons[num] = 1
    
    if len(nums) / 2 < len(pocketmons):
        return len(nums) / 2
    else:
        return len(pocketmons)
        