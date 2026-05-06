# import math

def maxNumber(value):
    digits = list(str(value))
    digits.sort(reverse=True)
    return int(''.join(digits))

def minNumber(value):
    digits = list(str(value))
    digits.sort()
    return int(''.join(digits))

def solution(num):
    answer = 0;
    maxNum = maxNumber(num)
    minNum = minNumber(num)

    answer = maxNum - minNum
    return answer
