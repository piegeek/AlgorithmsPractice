def func_a(arr):
    answer = -1
    for i in range(len(arr)):
        if answer == -1:
            answer = i
        elif arr[answer] < arr[i]:
            answer = i
    return answer


def func_b(arr1, arr2):
    answer = [0] * len(arr1)
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                answer[i] += 1
    return answer


def func_c(arr, count):
    answer = -1
    for idx, elem in enumerate(arr):
        if elem == count:
            continue
        if answer == -1:
            answer = idx
        elif arr[answer] < elem:
            answer += 1
    return answer


def solution(menu, votes):
    counter = func_b(menu, votes)
    first = func_a(counter)
    second = func_c(counter, counter[first])

    answer = [menu[first], menu[second]]
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
menu = ["Latte", "Americano","Espresso" ]
votes = ["Latte", "Americano", "Espresso", "Latte", "Americano", "Americano", "Latte", "Americano", "Americano", "Latte", "Latte", "Latte"]
ret = solution(menu, votes)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

menu = ["MochaLatte", "GreenTea", "Cappuccino"]
votes = ["GreenTea", "GreenTea", "MochaLatte", "GreenTea", "Cappuccino", "Cappuccino"]
ret = solution(menu, votes)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")