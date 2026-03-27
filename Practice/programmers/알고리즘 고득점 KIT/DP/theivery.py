def solution(money):
    visited = 0
    
    n = len(money)
    
    cache = {}
    
    ret = dp(0, visited, money, n, cache)
    
    return ret

def dp(idx, visited, money, n, cache):
    if idx == n:
        return 0
    
    if (idx, visited) in cache:
        return cache[(idx, visited)]
    
    ret = 0
    
    # Skip idx
    ret = max(ret, dp(idx+1, visited, money, n, cache))
    
    # Take idx
    if not (visited & (1 << ((idx-1) % n))) and not (visited & (1 << (idx+1 % n))):
        visited |= (1 << idx)
        ret = max(ret, money[idx] + dp(idx+1, visited, money, n, cache))
        visited &= ~(1 << idx)
    
    cache[(idx, visited)] = ret
    return ret