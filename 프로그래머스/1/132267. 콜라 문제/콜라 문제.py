import sys
import math

def solution(a, b, n):
    result = 0
    while n >= a:
        s = n % a
        c = (n-s) / a * b
        n = c + s
        result += c 
    return result