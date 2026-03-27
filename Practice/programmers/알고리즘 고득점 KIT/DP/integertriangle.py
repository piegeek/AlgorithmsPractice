def solution(triangle):
    cache = {}
    
    ret = dp(0, 0, triangle, cache)
    
    return ret

def dp(i, j, triangle, cache):
    if i == len(triangle):
        return 0
    
    if (i, j) in cache:
        return cache[(i, j)]
    
    ret = 0
    
    # Take j
    ret = max(ret, triangle[i][j] + dp(i+1, j, triangle, cache))
    
    # Take j + 1
    ret = max(ret, triangle[i][j] + dp(i+1, j+1, triangle, cache))
    
    cache[(i, j)] = ret
    return ret
    
    