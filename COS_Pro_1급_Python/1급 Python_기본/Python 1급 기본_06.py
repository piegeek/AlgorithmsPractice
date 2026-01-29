def solution(start, locations):
    answer = 0
    min = 0 
    max = 0
    for i in locations:
        if i < min:
            min = i
        if i > max:
            max = i
            
    if start <= min:
        answer = max - start
    elif start >= max:
        answer = start - min
    else:
        if start - min < max - start:
            answer = start - min + (max - min)
        else:
            answer = max - start + (max - min)
            
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
start = 15
locations = [10, 62, 22]
ret = solution(start, locations)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")