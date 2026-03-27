def solution(k, dungeons):
    visited = 0
    
    ret = 0
    
    cache = {}
    
    for i in range(len(dungeons)):
        if k >= dungeons[i][0]:
            visited |= (1 << i)
            next_k = k - dungeons[i][1]
            ret = max(ret, 1 + dp(visited, next_k, dungeons, cache))
            visited &= ~(1 << i)
            
    return ret

def dp(visited, k, dungeons, cache):
    if (visited, k) in cache:
        return cache[(visited, k)]
    
    ret = 0
    
    for i in range(len(dungeons)):
        if not (visited & (1 << i)) and k >= dungeons[i][0]:
            visited |= (1 << i)
            next_k = k - dungeons[i][1]
            ret = max(ret, 1 + dp(visited, next_k, dungeons, cache))
            visited &= ~(1 << i)
           
    cache[(visited, k)] = ret
    return ret
            