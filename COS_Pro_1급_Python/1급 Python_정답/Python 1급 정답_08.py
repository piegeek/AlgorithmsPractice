# import math

def solution(numberA, numberB, limit):
    answer = [0] * 1001
    answer[0] = 1
    for number in range(min(numberA, numberB), limit + 1):
        if number - numberA >= 0 and answer[number - numberA] == 1:
            answer[number] = 1
        if number - numberB >= 0 and answer[number - numberB] == 1:
            answer[number] = 1   
    return sum(answer[1:])
