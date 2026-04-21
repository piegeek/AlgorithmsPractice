import heapq

def solution(priorities, location):
    queue = []
    for i in range(len(priorities)):
        heapq.heappush(queue, (-priorities[i], i))
        
    n = len(queue)
        
    count = 1
    
    # print(f'init: queue: {queue}')
    
    while len(queue) > 0:
        priority, idx = heapq.heappop(queue)
        
        # print(f'before: queue: {queue}')
        
        queue = sorted(queue, key = lambda x : (x[1] - idx) % n)
        
        # print(f'after: queue: {queue}')
        
        if idx == location:
            return count
        
        count += 1
        
    return count
    