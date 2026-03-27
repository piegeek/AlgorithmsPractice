# Use visited for array traversals too!!!!
import math

def solution(progresses, speeds):
    times = []
    
    for i in range(len(progresses)):
        times.append(math.ceil((100 - progresses[i]) / speeds[i]))
        
    # print(times)
        
    output = []
            
    visited = [False for _ in range(len(times))]
            
    for i in range(len(times)):
        if visited[i] == False:
            idx = i
            count = 0
            while idx < len(times) and times[i] >= times[idx]:
                visited[idx] = True
                idx += 1
                count += 1
                
            output.append(count)
            
    
    return output