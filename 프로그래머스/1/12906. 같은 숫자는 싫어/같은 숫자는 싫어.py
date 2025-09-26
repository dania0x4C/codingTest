def solution(arr):
    sortedArr = []
    preI = -1
    for i in arr:
        if preI != i:
            sortedArr.append(i)
        preI = i
    return sortedArr