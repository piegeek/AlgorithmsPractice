import copy
import sys

sys.setrecursionlimit(10 ** 6)

def solution(number, k):
    ret = 0
    
    n = len(number)
    
    stack = []
    combs = []
    n_choose_k(0, 0, number, n, k, stack, combs)
    
    for comb in combs:
        comp = [number[i] for i in range(n) if i not in comb]
        comp_int = int(''.join(comp))
        ret = max(ret, comp_int)
        
    return str(ret)
    
def n_choose_k(idx, chosen, number, n, k, stack, combs):
    if idx > n:
        return
    
    if chosen == k:
        stack_copy = copy.deepcopy(stack)
        combs.append(stack_copy)
        return
    
    # Skip idx
    # Why -1 here? (Off by one) -> My original code was correct; 1 should not be subtracted
    # if n - idx + chosen - 1 >= k:
    if n - idx + chosen >= k:
        n_choose_k(idx+1, chosen, number, n, k, stack, combs)
        
    # Take idx
    if chosen + 1 <= k:
        stack.append(idx)
        n_choose_k(idx+1, chosen+1, number, n, k, stack, combs)
        stack.pop(-1)

def solution_greedy(number, k):
    max_size = len(number) - k

    E = list(enumerate(number))

    E = sorted(E, key = lambda x : (-int(x[1]), x[0]))

    S = []

    for i, digit in E:
        cand = sorted(S + [(i, digit)], key = lambda x : x[0])

        if len(cand) > max_size:
            continue

        independent = all(ci <= t + k for t, (ci, d) in enumerate(cand))

        if independent:
            S = cand

    return ''.join(d for _, d in S)

def solution_greedy_correct(number, k):
    stack = []
    
    for digit in number:
        while k > 0 and stack and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # If k still remains, remove from the end
    return ''.join(stack[:len(stack) - k])