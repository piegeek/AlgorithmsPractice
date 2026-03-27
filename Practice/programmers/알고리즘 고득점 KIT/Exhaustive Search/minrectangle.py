# This solution TLE's...
import copy

INF = 10 ** 9

def solution(sizes):
    combs = []
    stack = []
    
    decision_dp(0, sizes, stack, combs)
    
    # print(combs)
    
    ret = INF
    
    for comb in combs:
        max_w = max([x[0] for x in comb])
        max_h = max([x[1] for x in comb])
        ret = min(ret, max_w * max_h)
        
    return ret
    
def decision_dp(idx, sizes, stack, combs):
    if idx == len(sizes):
        stack_copy = copy.deepcopy(stack)
        combs.append(stack_copy)
        return
        
    # Dont flip
    stack.append(sizes[idx])
    decision_dp(idx+1, sizes, stack, combs)
    stack.pop(-1)
    
    # Flip
    stack.append(sizes[idx][::-1])
    decision_dp(idx+1, sizes, stack, combs)
    stack.pop(-1)
    