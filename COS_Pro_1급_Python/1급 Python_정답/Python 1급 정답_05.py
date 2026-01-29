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
            answer = idx #here
    return answer


def solution(menu, votes):
    counter = func_b(menu, votes)
    first = func_a(counter)
    second = func_c(counter, counter[first])

    answer = [menu[first], menu[second]]
    return answer