INF = 10 ** 9

def solution(arr):
    n = int((len(arr) - 1) / 2)
    nums = list(map(int, [arr[i] for i in range(len(arr)) if i % 2 == 0]))
    operators = [arr[i] for i in range(len(arr)) if i % 2 != 0]
    
    cache = {}
    
    ret = dp(0, n, nums, operators, cache)
    
    return ret
    
def dp(left, right, nums, operators, cache):
    if right == left:
        return nums[left]
    
    if (left, right) in cache:
        return cache[(left, right)]
    
    ret = (-1) * INF
    
    for i in range(left, right):
        if operators[i] == '-':
            ret = max(ret, dp(left, i, nums, operators, cache) - dp(i+1, right, nums, operators, cache))
            
        if operators[i] == '+':
            ret = max(ret, dp(left, i, nums, operators, cache) + dp(i+1, right, nums, operators, cache))
    
    cache[(left, right)] = ret
    return ret