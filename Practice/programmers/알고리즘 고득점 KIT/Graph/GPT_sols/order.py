def solution(n, results):
    win_graph = [[] for _ in range(n)]
    lose_graph = [[] for _ in range(n)]
    
    for a, b in results:
        a -= 1
        b -= 1
        win_graph[a].append(b)   # a beats b
        lose_graph[b].append(a)  # b loses to a
    
    def dfs(start, graph):
        visited = [False] * n
        stack = [start]
        count = 0
        
        while stack:
            node = stack.pop()
            for nxt in graph[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append(nxt)
                    count += 1
        return count
    
    answer = 0
    
    for i in range(n):
        win = dfs(i, win_graph)
        lose = dfs(i, lose_graph)
        
        if win + lose == n - 1:
            answer += 1
            
    return answer