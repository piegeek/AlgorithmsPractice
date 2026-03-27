import heapq

def solution(scoville, K):
    queue = []
    
    for i in range(len(scoville)):
        heapq.heappush(queue, scoville[i])
        
    step = 0
        
    while len(queue) > 0:
        if all_over_K(queue, K):
            return step
        
        if len(queue) >= 2: 
            first = heapq.heappop(queue)
            second = heapq.heappop(queue)

            heapq.heappush(queue, first + 2 * second)
        
            step += 1
        else:
            return -1
        
def all_over_K(queue, K):
    for i in range(len(queue)):
        if queue[i] < K:
            return False
        
    return True
        
        
        