# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def func_a(arr):
    ret = []
    for a in arr:
        a.sort()
        ret.append(a[1:-1])
    return ret

def func_b(arr):
    ret  = []
    for a in arr:
        sum = 0
        for b in a:
            sum += b
        sum = int(sum / len(a))
        ret.append(sum)
    ret.sort(reverse=True)
    return ret[0]


def solution(scores):
    arr = func_a(scores)
    answer = func_b(arr)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores = [[85, 92, 95, 90], [91, 76, 85, 50]]
ret = solution(scores)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
