def solution(N, number):
    avail_Ns = list(map(int, [ str(N) * i for i in range(1, 8+1) ]))
    
    print(avail_Ns)
    
    combs1 = []
    
    for n1 in avail_Ns:
        for n2 in avail_Ns:
            combs1.append(n1 + n2)
            combs1.append(n1 - n2)
            combs1.append(n1 * n2)
            if n2 != 0:
                combs1.append(n1 // n2)
                
    total_combs = []
    generate_combs(combs1, 1, 4, total_combs)
    
    for idx, comb in enumerate(total_combs):
        if number in comb:
            return idx
        
    return -1
    
def generate_combs(combs, curr, n, total_combs):
    if curr == n:
        return
    
    next_combs = []
    
    for n1 in combs:
        for n2 in combs:
            next_combs.append(n1 + n2)
            next_combs.append(n1 - n2)
            next_combs.append(n1 * n2)
            if n2 != 0:
                next_combs.append(n1 // n2)
                
    total_combs.append(next_combs)
                
    generate_combs(next_combs, curr + 1, n, total_combs)
    
    
if __name__ == '__main__':
	print(solution(5, 12))