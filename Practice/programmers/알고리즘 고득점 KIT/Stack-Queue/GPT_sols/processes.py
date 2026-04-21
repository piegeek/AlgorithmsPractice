import heapq
from collections import deque

def solution(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    
    # max heap
    max_heap = [-p for p in priorities]
    heapq.heapify(max_heap)
    
    count = 0
    
    while queue:
        p, i = queue.popleft()
        
        # compare with current max
        if p < -max_heap[0]:
            queue.append((p, i))
        else:
            count += 1
            heapq.heappop(max_heap)
            
            if i == location:
                return count