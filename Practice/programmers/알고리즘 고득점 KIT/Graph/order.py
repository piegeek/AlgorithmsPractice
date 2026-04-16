# GPT-aided solution
def solution(n, results):
    win_graph = [[] for _ in range(n)]
    lose_graph = [[] for _ in range(n)]
    
    # Zero indexing
    for i in range(len(results)):
        results[i][0] -= 1
        results[i][1] -= 1
        
    for i in range(len(results)):
        win_graph[results[i][0]].append(results[i][1])
        lose_graph[results[i][1]].append(results[i][0])
        
    ret = 0
    
    for i in range(n):
        win_visited = [False for _ in range(n)]
        lose_visited = [False for _ in range(n)]
        
        win_visited[i] = True
        lose_visited[i] = True
        
        win = dfs(i, win_graph, win_visited) - 1
        lose = dfs(i, lose_graph, lose_visited) - 1
        
        # print('---')
        # print(win)
        # print(lose)
        
        if win + lose == n - 1:
            ret += 1
            
    return ret

def dfs(last, graph, visited):
    ret = 1
    
    for v in graph[last]:
        if not visited[v]:
            visited[v] = True
            ret += dfs(v, graph, visited)
            
    return ret
        

# I feel like this has something to do with topological sort
def solution(n, results):
    v_in = [0 for _ in range(n)]
    v_out = [0 for _ in range(n)]
    adj_list = [[] for _ in range(n)]
    
    # Zero indexing
    for i in range(len(results)):
        results[i][0] -= 1
        results[i][1] -= 1
        
    for i in range(len(results)):
        v_out[results[i][0]] += 1
        v_in[results[i][1]] += 1
        adj_list[results[i][0]].append(results[i][1])
        
    confirmed = []
        
    for i in range(n):
        if v_in[i] + v_out[i] == n - 1:
            confirmed.append(i)
            
    for c in confirmed:
        for v in adj_list[c]:
            dfs(v, confirmed, adj_list)
            
    print(confirmed)
    
    return len(confirmed)
            
def dfs(last, confirmed, adj_list):
    if last not in confirmed:
        confirmed.append(last)
    for v in adj_list[last]:
        dfs(v, confirmed, adj_list)
        