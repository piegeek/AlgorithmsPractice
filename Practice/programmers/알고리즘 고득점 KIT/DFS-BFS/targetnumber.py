# My code TLE's...
import copy

def solution(numbers, target):
    operations = ['+', '-']
    
    n = len(numbers)
    
    combs = []
    decision_dp(0, n, [], combs)
    
    # print(combs)
    
    ret = 0
    
    for comb in combs:
        if comb[0] == '+':
            num = numbers[0]
        else:
            num = (-1) * numbers[0]
            
        for j in range(1, len(comb)):
            if comb[j] == '+':
                num += numbers[j]
            else:
                num -= numbers[j]
                
        if num == target:
            ret += 1
            
    return ret
    
def decision_dp(idx, n, stack, combs):
    if idx == n:
        stack_copy = copy.deepcopy(stack)
        combs.append(stack_copy)
        return
    
    # Take '+'
    stack.append('+')
    decision_dp(idx+1, n, stack, combs)
    stack.pop(-1)
    
    # Take '-'
    stack.append('-')
    decision_dp(idx+1, n, stack, combs)
    stack.pop(-1)
        