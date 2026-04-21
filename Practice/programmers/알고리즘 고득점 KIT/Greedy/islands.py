def solution(n, costs):
    costs = sorted(costs, key = lambda x : x[2])
    
    ret = 0
    
    S = []
    
    parents = [x for x in range(n)]
    
    for e in costs:
        cand = S + [e]
        if is_independent(cand, parents):
            ret += e[2]
            S = cand
        
    return ret

def is_independent(cand, parents):
    for edge in cand:
        u, v, cost = edge
        
        if find(u, parents) == find(v, parents):
            return False
        
    return True

def find(u, parents):
    while parents[u] != u:
        u = parents[u]
        
    return u

def union(u, v, parents):
    u = find(u, parents)
    v = find(v, parents)
    parents[v] = u
        