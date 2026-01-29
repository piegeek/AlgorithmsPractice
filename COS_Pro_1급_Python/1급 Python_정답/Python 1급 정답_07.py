ALPHANUM = 26


def func1(number, arr1, arr2):
    arr2[number] = True
    for i in range(ALPHANUM):
        if arr1[number][i] and not arr2[i]:
            func1(i, arr1, arr2)

def func2(arr):
    answer = 0
    for value in arr:
        if value: #here
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