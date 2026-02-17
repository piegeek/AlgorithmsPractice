INF = 1000 * 1000

def solution(n, m, hole):
    board = [ [ 0 for _ in range(n) ] for _ in range(m) ]
    visited = [ [ False for _ in range(n) ] for _ in range(m) ]
    
    for h in hole:
        a, b = h
        board[m - b][a-1] = 1
        
    board[0][n-1] = 9
    
    ret = INF
    
    for shoe_used in [True, False]:
        ret = min(ret, dfs(m-1, 0, m, n, board, visited, shoe_used))
        
    if ret == INF:
        return -1
        
    return ret
    
def dfs(i, j, m, n, board, visited, shoe_used):
    moves = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0]
    ]
    
    if (i, j) == (0, n-1):
        return 0
    
    visited[i][j] = True
    
    ret = INF
    
    if shoe_used == True:
        for move in moves:
            dy, dx = move
            if 0 <= i + dy and i + dy <= m-1 and 0 <= j + dx and j + dx <= n-1 and visited[i+dy][j+dx] == False and board[i+dy][j+dx] != 1:
                ret = min(ret, 1 + dfs(i+dy, j+dx, m, n, board, visited, shoe_used))
    else:
        # Try using shoe
        for move in moves:
            dy, dx = move
            dy *= 2
            dx *= 2
            if 0 <= i + dy and i + dy <= m-1 and 0 <= j + dx and j + dx <= n-1 and visited[i+dy][j+dx] == False and board[i+dy][j+dx] != 1:
                ret = min(ret, 1 + dfs(i+dy, j+dx, m, n, board, visited, True))
        # Dont use shoe
        for move in moves:
            dy, dx = move
            if 0 <= i + dy and i + dy <= m-1 and 0 <= j + dx and j + dx <= n-1 and visited[i+dy][j+dx] == False and board[i+dy][j+dx] != 1:
                ret = min(ret, 1 + dfs(i+dy, j+dx, m, n, board, visited, False))
    
    visited[i][j] = False
    
    return ret  
                
        
    
