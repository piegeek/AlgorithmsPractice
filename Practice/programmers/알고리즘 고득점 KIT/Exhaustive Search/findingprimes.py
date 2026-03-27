import itertools
import copy

def solution(numbers):
    nums = list(numbers)
    
    combs = []
    
    for k in range(1, len(numbers)+1):
        comb = list(map(list, itertools.combinations(nums, k)))
        
        for c in comb:
            combs.append(c)
        
    # print(combs)
        
    out = []
    for comb in combs:
        perm = itertools.permutations(comb)
        for p in perm:
            x = int(''.join(list(p)))
            out.append(x)
    
    out = list(set(out))
    
    ret = 0
    
    for o in out:
        if is_prime(o):
            ret += 1
            
    return ret

def is_prime(num):
    if num < 2: return False
    if num == 2: return True

    for x in range(2, int(num ** (1/2)) + 1):
        if num % x == 0:
            return False
        
    return True
        