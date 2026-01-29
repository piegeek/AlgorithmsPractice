import math

def solution(money, cost, name):
    answer = ""
    max_distance = 0

    i = 0
    while i < len(cost):
        oil = math.trunc(money / [[quiz]])
        distance = [[quiz]] * [[quiz]]
        if distance > [[quiz]]:
            max_distance = distance
            answer = [[quiz]]
        i += 1
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
money = 100000
cost = [[50, 5000], [20, 1000], [20, 5000], [50, 1000]]
name = ["A", "B", "C", "D"]
ret = solution(money, cost, name)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")