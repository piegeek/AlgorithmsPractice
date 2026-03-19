import itertools

MOD = 10007

def solution(n, tops):
    ret = dp(n, tops)
    return ret

def dp(n, tops):
    ret = 0
    
    tops_indices = [idx for idx in range(n) if tops[idx] == 1]
    print(tops_indices)
    
    for k in range(1, len(tops_indices)+1):
        n_choose_k = choose(n, k)
        
        combs = itertools.combinations(tops_indices, k)
        
        x_last = 0
        
        count = 1
        
        for comb in combs:
            print(comb)
            for xi in comb:
                count *= count_a(xi - x_last)
                x_last = xi
            count *= count_a(n - x_last)
                
        ret += n_choose_k * count
        ret %= MOD
        
    return ret

def count_a(n):
    if n in [0, 1]:
        return 1

    ret = 0
    for i in range(n):
        ret += count_a(i)
        
    return ret

def choose(n, k):
    return fact(n) / (fact(n-k) * fact(k))

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
                