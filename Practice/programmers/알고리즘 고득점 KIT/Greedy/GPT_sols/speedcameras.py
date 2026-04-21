INF = 10 ** 9

def solution(routes):
    ret = 0
    
    routes = sorted(routes, key = lambda x : x[1])
    
    camera = -INF
    
    for start, end in routes:
        if start > camera:
            ret += 1
            camera = end
            
    return ret
        