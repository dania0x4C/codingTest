def solution(numbers):
    result = ''
    changeStrings = map(str, numbers)
    sortedNumbers = sorted(changeStrings, key = lambda x: x*3, reverse = True)
    
    for sortedNumber in sortedNumbers:
        result += sortedNumber
        
    if result[0] == '0':
        return '0'
    else:
        return result