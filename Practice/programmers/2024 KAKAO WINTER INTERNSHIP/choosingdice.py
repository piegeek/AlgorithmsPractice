import copy

def solution(dice):
    n = len(dice)
    combs = []
    get_combs(1, 0, [], combs, dice, n)
    
    res = [[ 0, 0, 0 ] for _ in range(len(combs))]
    ret = 0
    max_prob = 0
    
    for idx, comb in enumerate(combs):
        a_dies = comb
        b_dies = [ x for x in range(1, n+1) if x not in comb ]
        
        # print(a_dies)
        # print(b_dies)
        
        a_scores = []
        stack = []
        for i in range(6):
            stack.append(dice[a_dies[0] - 1][i])
            dfs(1, a_dies, dice, stack, a_scores, n)
            stack.pop(-1)
            
        # print(a_scores)
            
        b_scores = []
        stack = []
        for i in range(6):
            stack.append(dice[b_dies[0] - 1][i])
            dfs(1, b_dies, dice, stack, b_scores, n)
            stack.pop(-1)
            
        # print(a_scores)
        # print(b_scores)
            
        for a_score in a_scores:
            for b_score in b_scores:
                if a_score > b_score:
                    res[idx][0] += 1
                elif a_score < b_score:
                    res[idx][2] += 1
                elif a_score == b_score:
                    res[idx][1] += 1
                    
        new_prob = res[idx][0] / sum(res[idx])
        if new_prob > max_prob:
            max_prob = new_prob
            ret = idx
            
    return sorted(combs[ret])
        
def dfs(idx, dies, dice, stack, scores, n):
    if len(stack) == n / 2:
        scores.append(sum(stack))
        return
        
    for i in range(6):
        stack.append(dice[dies[idx] - 1][i])
        dfs(idx+1, dies, dice, stack, scores, n)
        stack.pop(-1)
    
def get_combs(idx, chosen, stack, combs, dice, n):
    # Why n+2 here???
    if idx == n+2:
        return
    
    if chosen == n / 2:
        stack_copy = copy.deepcopy(stack)
        combs.append(stack_copy)
        return
    
    # Skip
    get_combs(idx+1, chosen, stack, combs, dice, n)
    
    # Take
    stack.append(idx)
    get_combs(idx+1, chosen+1, stack, combs, dice, n)
    stack.pop(-1)
        