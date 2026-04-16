import heapq

def solution(routes):
    ret = 0
    
    start = min([x[0] for x in routes])
    end = max([x[1] for x in routes])
    
    t = start
    
    route_idx = 0
    
    queue = []
    
    routes = sorted(routes, key = lambda x : x[0])
    
    while t <= end:
        if len(queue) > 0 and t == queue[0][0]:
            heapq.heappop(queue)
        
        if route_idx < len(routes) and t == routes[route_idx][0]:
            heapq.heappush(queue, (routes[route_idx][1], routes[route_idx]))
            route_idx += 1
            
        ret = max(ret, len(queue))
            
        t += 1
            
    return ret
            
            
            
    