def solution(projects):
    projects.sort(key=lambda x: x[0], [[quiz]])
    projects.sort(key=lambda x: x[2], [[quiz]])
    projects.sort(key=lambda x: x[1], [[quiz]])
    answer = [[quiz]]
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
projects = [[5, 90, 90], [1, 90, 70], [3, 95, 70], [2, 85, 85], [4, 70, 90]]
ret = solution(projects)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")