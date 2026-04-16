def solution(n, lost, reserve):
    ret = n - len(lost)
    visited = [False for _ in range(len(reserve))]
    
    ret = max(ret, dp(0, n, lost, reserve, visited))
    
    return ret

def dp(idx, n, lost, reserve, visited):
    ret = n - len(lost)
    
    if idx == len(lost):
        return ret
    
    # Skip idx
    ret = max(ret, dp(idx+1, n, lost, reserve, visited))
    
    # Take idx
    min_one_idx = find_index(reserve, lost[idx] - 1)
    
    if min_one_idx != -1 and visited[min_one_idx] == False and reserve[min_one_idx] not in lost:
        visited[min_one_idx] = True
        ret = max(ret, 1 + dp(idx+1, n, lost, reserve, visited))
        visited[min_one_idx] = False
        
    plus_one_idx = find_index(reserve, lost[idx] + 1)
    
    if plus_one_idx != -1 and visited[plus_one_idx] == False and reserve[plus_one_idx] not in lost:
        visited[plus_one_idx] = True
        ret = max(ret, 1 + dp(idx+1, n, lost, reserve, visited))
        visited[plus_one_idx] = False
    
    eq_idx = find_index(reserve, lost[idx])
    if eq_idx != -1:
        visited[eq_idx] = True
        ret = max(ret, 1 + dp(idx+1, n, lost, reserve, visited))
        
    return ret
    
def find_index(lst, item):
    for i in range(len(lst)):
        if item == lst[i]:
            return i
        
    return -1