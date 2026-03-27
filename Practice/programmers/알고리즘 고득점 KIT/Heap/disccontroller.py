'''
Find out why my code TLE's
'''
import heapq

def solution(jobs):
    # State
    wait_queue = []
    run_queue = []
    
    t = 0
    process_t = 0
    
    job_idx = 0
    
    delay = [-1 for _ in range(len(jobs))]
    
    while job_idx < len(jobs) or len(run_queue) > 0 or len(wait_queue) > 0:
        if len(run_queue) > 0 and process_t == run_queue[0][1]:
            job = run_queue.pop(-1)
            process_t = 0
            delay[jobs.index(job)] = t - job[0]
        
        if job_idx < len(jobs) and t == jobs[job_idx][0]:
            job = jobs[job_idx]
            heapq.heappush(wait_queue, ((job[1], job[0], job_idx), job))
            job_idx += 1
            
        if len(run_queue) == 0 and len(wait_queue) > 0:
            priority, job = heapq.heappop(wait_queue)
            run_queue.append(job)
            process_t = 0
            
        # print(f't: {t}, run_queue: {run_queue}, wait_queue: {wait_queue}')
            
        t += 1
        process_t += 1
            
    return int(sum(delay) / len(delay))
            