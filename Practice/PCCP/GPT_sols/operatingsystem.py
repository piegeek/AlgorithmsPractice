import heapq

def solution(program):
    program.sort(key=lambda x: x[1])  # sort by arrival
    
    n = len(program)
    heap = []
    time = 0
    i = 0
    
    waiting_sum = [0] * 11
    
    while i < n or heap:
        
        # If no job running, jump to next arrival
		# Arrival time is greater than current time -> Jump to arrival time
        if not heap and time < program[i][1]:
            time = program[i][1]
        
        # Add all jobs that arrived
        while i < n and program[i][1] <= time:
            score, arrival, duration = program[i]
            heapq.heappush(heap, (score, arrival, duration))
            i += 1
        
        score, arrival, duration = heapq.heappop(heap)
        
        waiting_sum[score] += time - arrival
        time += duration
    
    waiting_sum[0] = time
    return waiting_sum
