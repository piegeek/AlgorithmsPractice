import math

def solution(money, cost, name):
    answer = ""
    max_distance = 0

    i = 0
    while i < len(cost):
        oil = math.trunc(money / cost[i][1])
        distance = cost[i][0] * oil
        if distance > max_distance:
            max_distance = distance
            answer = name[i]
        i += 1
    return answer