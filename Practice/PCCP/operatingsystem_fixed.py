import heapq

def solution(program):
    program = sorted(program, key = lambda x : x[1])
       
    # Event, State
    # events - 1. curr_time becomes first start time 2. currently running program ends, 3. curr_time hits when first process in wait queue can be run
    # states - current_time, curr_duration, heap to hold processes in wait, heap to hold currently running process
    
    heap_wait = []
    heap_runn = []
    
    # curr_time - even though its state; updated last (think of for loops)
    curr_time = -1
    curr_duration = -1
    
    # Output 
    ret = [ 0 for _ in range(11) ]
    
    while (len(program) > 0 or len(heap_wait) > 0 or len(heap_runn) > 0):
        # State update
        curr_time += 1
        curr_duration += 1
        
        # Don't mix invariant checking and state transitions
        # (Invariant checking <=> Event checking) different
        
        # Event - curr_time hits when program must be pushed into queue
		# Order of event checking statements - follows intermediate state transition logic
        while len(program) > 0 and curr_time == program[0][1]:
            # State update
            heapq.heappush(heap_wait, (program[0][0], program[0]))
            program.pop(0)
            
            # State evalutaion
            pass
        
        # Event - process ends
        if len(heap_runn) == 1:
            running_process = heap_runn[0]
            # State evaluation (invariant: curr_duration < runtime)
            if curr_duration == running_process[2]:
                heap_runn.pop(0)
                curr_duration = 0
            
        # Event - curr_time hits when program in wait queue can be run
        if len(heap_runn) == 0:
            if len(heap_wait) > 0:
                next_process = heap_wait[0][1]
                if curr_time >= next_process[1]:
                    heapq.heappop(heap_wait)
                    heap_runn.append(next_process)
                    curr_duration = 0
                    
                    # Determine output
                    score = next_process[0]
                    wait_time = curr_time - next_process[1]
                    ret[score] += wait_time
                    
    ret[0] = curr_time
    
    return ret
    