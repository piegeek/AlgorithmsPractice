ALPHANUM = 26


def func1(number, arr1, arr2):
    arr2[number] = True
    for i in range(ALPHANUM):
        if arr1[number][i] and not arr2[i]:
            func1(i, arr1, arr2)

def func2(arr):
    answer = 0
    for value in arr:
        if not value:
            answer += 1
    return answer

def func3(arr1, arr2):
    for elem1, elem2 in arr1:
        num1, num2 = ord(elem1) - ord('A'), ord(elem2) - ord('A')
        arr2[num1][num2] = True
        arr2[num2][num1] = True


def solution(list):
    graph = [[False for _ in range(ALPHANUM)] for _ in range(ALPHANUM)]
    visited = [False] * ALPHANUM

    func3(list, graph)
    visited[0] = True
    for node in range(ALPHANUM):
        if graph[0][node] and not visited[node]:
            func1(node, graph, visited)
    return func2(visited)

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
list = ["AB", "BC", "DE", "CF"]
ret = solution(list)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")