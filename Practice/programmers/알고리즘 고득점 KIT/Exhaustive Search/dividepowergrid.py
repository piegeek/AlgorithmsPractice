def solution(n, wires):
    ret = n
    
    for i in range(len(wires)):
        edges = wires[:i] + wires[i+1:]
        
        adj_list = create_adj_list(n, edges)
        
        # Zero-indexing
        v1 = wires[i][0] - 1
        v2 = wires[i][1] - 1
        
        visited1 = (1 << v1)
        visited2 = (1 << v2)
        
        cache = {}
        
        connected1 = dfs(v1, adj_list, visited1, cache)
        connected2 = dfs(v2, adj_list, visited2, cache)
        
        ret = min(ret, abs(connected1 - connected2))
        
    return ret

def dfs(last, adj_list, visited, cache):
    if (last, visited) in cache:
        return cache[(last, visited)]
    
    ret = 0
    
    for v in adj_list[last]:
        if not (visited & (1 << v)):
            visited |= (1 << v)
            ret += 1 + dfs(v, adj_list, visited, cache)
            visited &= ~(1 << v)
            
    cache[(last, visited)] = ret
    return ret
        
def create_adj_list(n, edges):
    adj_list = [[] for _ in range(n)]
    
    for edge in edges:
        v1, v2 = edge
        # Zero-indexing
        v1 -= 1
        v2 -= 1
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)
        
    return adj_list