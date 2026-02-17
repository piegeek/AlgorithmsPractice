from collections import deque

def solution(n, m, hole):
    board = [[0 for _ in range(n)] for _ in range(m)]
    
    for a, b in hole:
        board[m - b][a - 1] = 1
    
    visited = [[[False] * 2 for _ in range(n)] for _ in range(m)]
    
    q = deque()
    # (row, col, shoe_used, time)
    q.append((m - 1, 0, 0, 0))  # shoe_used = 0 (not used)
    visited[m - 1][0][0] = True
    
    moves = [(0,1), (1,0), (0,-1), (-1,0)]
    
    while q:
        i, j, shoe_used, time = q.popleft()
        
        if (i, j) == (0, n - 1):
            return time
        
        # Normal moves
        for dy, dx in moves:
            ni, nj = i + dy, j + dx
            if 0 <= ni < m and 0 <= nj < n:
                if board[ni][nj] == 0 and not visited[ni][nj][shoe_used]:
                    visited[ni][nj][shoe_used] = True
                    q.append((ni, nj, shoe_used, time + 1))
        
        # Use shoe if not used yet
        if shoe_used == 0:
            for dy, dx in moves:
                ni, nj = i + 2*dy, j + 2*dx
                if 0 <= ni < m and 0 <= nj < n:
                    if board[ni][nj] == 0 and not visited[ni][nj][1]:
                        visited[ni][nj][1] = True
                        q.append((ni, nj, 1, time + 1))
    
    return -1
