# import math

def maxNumber(value):
    digits = [ char for char in str(value) ]
    digits.sort(reverse = True)
    return int(''.join(digits))

def minNumber(value):
    digits = [ char for char in str(value) ]
    digits.sort(reverse = False)
    return int(''.join(digits))

def solution(num):
    answer = 0;
    maxNum = maxNumber(num)
    minNum = minNumber(num)

    answer = maxNum - minNum
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
num1 = 5924
ret1 = solution(num1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

num2 = 3904
ret2 = solution(num2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
