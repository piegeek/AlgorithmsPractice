import sys
import heapq

def solve_cupramen(N, problems):
    problems.sort(key=lambda x: x[0])  # sort by deadline
    
    heap = []
    
    for d, v in problems:
        heapq.heappush(heap, v)
        
        # if we exceed available time slots
        if len(heap) > d:
            heapq.heappop(heap)
    
    print(sum(heap))
