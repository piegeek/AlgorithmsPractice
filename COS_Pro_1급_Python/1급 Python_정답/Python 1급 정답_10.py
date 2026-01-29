def solution(household):
    household.sort(key=lambda x: x[0])
    household.sort(key=lambda x: x[3], reverse=True)
    household.sort(key=lambda x: x[2], reverse=True)
    household.sort(key=lambda x: x[1], reverse=True)
    answer = [i[0] for i in household]
    return answer