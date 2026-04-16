import heapq

INF = 10 ** 9

def solution(n, edge):
    # Zero-indexing
    for i in range(len(edge)):
        edge[i][0] -= 1
        edge[i][1] -= 1
    
    adj_list = [ [] for _ in range(n) ]
    
    for e in edge:
        v1, v2 = e
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)
        
    dist = [INF for _ in range(n)]
    dist[0] = 0
    
    dijkstra(dist, n, adj_list)
    
    farthest_dist = max(dist)
    ret = dist.count(farthest_dist)
    
    return ret
    
def dijkstra(dist, n, adj_list):
    queue = []
    
    heapq.heappush(queue, (0, 0))
    
    while len(queue) > 0:
        curr_dist, v = heapq.heappop(queue)
        
        for vertex in adj_list[v]:
            next_dist = 1 + curr_dist
            if dist[vertex] > next_dist:
                dist[vertex] = next_dist
                heapq.heappush(queue, (next_dist, vertex))
    

# DFS solution - incorrect interpretation of the problem
def solution(n, edge):
    # Zero-indexing
    for i in range(n):
        edge[i][0] -= 1
        edge[i][1] -= 1
    
    adj_list = [ [] for _ in range(n) ]
    
    for e in edge:
        v1, v2 = e
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)
        
    max_dist = get_max_dist(n, adj_list)
    
    print(max_dist)
    
def get_max_dist(n, adj_list):
    visited = 0
    
    ret = 0
    
    for v in adj_list[0]:
        visited |= (1 << v)
        ret = max(ret, 1 + dfs(v, visited, n, adj_list))
        visited &= ~(1 << v)
        
    return ret

def dfs(last, visited, n, adj_list):
    ret = 0
    
    for v in adj_list[last]:
        if not (visited & (1 << v)):
            visited |= (1 << v)
            ret = max(ret, 1 + dfs(v, visited, n, adj_list))
            visited &= ~(1 << v)
            
    return ret
        
    
    