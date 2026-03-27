# Simulation Problem !!!
import itertools
import heapq

INF = 10 ** 9

def solution(bridge_length, weight, truck_weights):
    ret = get_duration(truck_weights, bridge_length, weight)        
    return ret

def get_duration(perm, bridge_length, weight):
    queue = []
    
    idx = 0
    
    time = 0
    
    while idx < len(perm) or len(queue) > 0: 
        if len(queue) > 0 and time - queue[0][0] == bridge_length:
            heapq.heappop(queue)
            
        if idx < len(perm) and sum([x[1] for x in queue]) + perm[idx] <= weight and len(queue) + 1 <= bridge_length:
            heapq.heappush(queue, (time, perm[idx]))
            idx += 1
            
        time += 1
            
    return time
        
        
    
        