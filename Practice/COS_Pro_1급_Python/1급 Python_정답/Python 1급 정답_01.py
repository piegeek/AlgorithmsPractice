def func_a(arr):
    ret = []
    for a in arr:
        a.sort()
        ret.append(a[1:len(a)-1])
    return ret

def func_b(arr):
    ret  = []
    for a in arr:
        sum = 0
        for b in a:
            sum += b
        sum = sum // len(a)
        ret.append(sum)
    ret.sort(reverse=True)
    return ret[0]


def solution(scores):
    arr2 = func_a(scores)
    answer = func_b(arr2)
    return answer