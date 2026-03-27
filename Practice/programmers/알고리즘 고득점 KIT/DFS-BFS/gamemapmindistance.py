# This TLE's...
INF = 10 ** 9

def solution(maps):
    moves = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0]
    ]
    
    n, m = len(maps[0]), len(maps)
    
    visited = [ [ False for _ in range(n) ] for _ in range(m) ]
    
    ret = INF
    
    for move in moves:
        dy, dx = move
        if 0 <= dy and dy <= m - 1 and 0 <= dx and dx <= n-1 and maps[dy][dx] == 1:
            visited[dy][dx] = True
            ret = min(ret, 1 + dfs(dy, dx, visited, n, m, moves, maps)) 
            visited[dy][dx] = False
            
    if ret == INF:
        return -1
    else:
        return ret
    
def dfs(i, j, visited, n, m, moves, maps):
    if (i, j) == (m-1, n-1):
        return 1
    
    ret = INF
    
    for move in moves:
        dy, dx = move
        if 0 <= i + dy and i + dy <= m-1 and 0 <= j + dx and j + dx <= n-1 and visited[i+dy][j+dx] == False and maps[i+dy][j+dx] == 1:
            visited[i+dy][j+dx] = True
            ret = min(ret, 1 + dfs(i + dy, j + dx, visited, n, m, moves, maps)) 
            visited[i+dy][j+dx] = False
            
    return ret
    