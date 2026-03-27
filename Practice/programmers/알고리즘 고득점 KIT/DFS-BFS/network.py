# Bitmask solution - here visited doesn't get modified inside dfs()
def solution(n, computers):
    parents = [ -1 for i in range(n) ]
    
    visited = 0
    for i in range(n):
        if not (visited & (1 << i)):
            visited |= (1 << i)
            print(f'before: {visited}')
            dfs(i, visited, i, parents, n, computers)
            print(f'after: {visited}')
            
    # print(parents)
            
def dfs(last, visited, root, parents, n, computers):
#     print(parents)
    
    parents[last] = root
    
    neighbors = [idx for idx in range(n) if computers[last][idx] == 1]
    
    for v in neighbors:
        if not (visited & (1 << v)):
            visited |= (1 << v)
            dfs(v, visited, root, parents, n, computers)

# Array solution - here visited gets modified inside dfs()
def solution(n, computers):
    parents = [ -1 for i in range(n) ]
    
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            print(f'before: {visited}')
            dfs(i, visited, i, parents, n, computers)
            print(f'after: {visited}')
            
    print(parents)
            
def dfs(last, visited, root, parents, n, computers):
#     print(parents)
    
    parents[last] = root
    
    neighbors = [idx for idx in range(n) if computers[last][idx] == 1]
    
    for v in neighbors:
        if not visited[v]:
            visited[v] = True
            dfs(v, visited, root, parents, n, computers)

# Final solution
def solution(n, computers):
    parents = [ -1 for i in range(n) ]
    
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(i, visited, i, parents, n, computers)
            
    parents = set(parents)
    return len(parents)
            
def dfs(last, visited, root, parents, n, computers):
    parents[last] = root
    
    neighbors = [idx for idx in range(n) if computers[last][idx] == 1]
    
    for v in neighbors:
        if not visited[v]:
            visited[v] = True
            dfs(v, visited, root, parents, n, computers)