def solution(diffs, times, limit):
    n = len(diffs)
    
    # Binary Search Approach??? - TODO -> Implemented
    level = 1

    lo = 1
    hi = 10 ** 5

    mid = (lo + hi) // 2
    
    for it in range(100):
        mid = (lo + hi) // 2

        if less_than(mid, n, diffs, times, limit):
            hi = mid
        else:
            lo = mid
        
    if less_than(mid, n, diffs, times, limit) == False:
        return mid + 1
    return mid 

def less_than(level, n, diffs, times, limit):
    elapsed = 0
    
    for i in range(n):
        if diffs[i] <= level:
            elapsed += times[i]
        elif diffs[i] > level:
            num_incorrect = diffs[i] - level
            elapsed += (times[max(0, i-1)] + times[i]) * num_incorrect + times[i]
            
        if elapsed > limit:
            return False

    if elapsed <= limit:
        return True
    else:
        return False

