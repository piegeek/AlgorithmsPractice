INF = 10 ** 9

def solution(rectangle, characterX, characterY, itemX, itemY):
    moves = [
        [1, 0],
        [0, -1],
        [-1, 0],
        [0, 1]
    ]
    
    ret = INF
    
    visited = [[False for _ in range(50+1)] for _ in range(50+1)]
    
    for move in moves:
        dx, dy = move
        if 1 <= characterX + dx and characterX + dx <= 50 and 1 <= characterY + dy and characterY + dy <= 50 and is_on_edge(rectangle, characterX + dx, characterY + dy):
            visited[characterX + dx][characterY + dy] = True
            
            ret = min(ret, 1 + dfs(characterX + dx, characterY + dy, visited, rectangle, itemX, itemY, moves))
            
            visited[characterX + dx][characterY + dy] = False
            
    return ret

def dfs(x, y, visited, rectangle, itemX, itemY, moves):
    if x == itemX and y == itemY:
        return 0
    
    ret = INF
    
    for move in moves:
        dx, dy = move
        
        if 1 <= x + dx and x + dx <= 50 and 1 <= y + dy and y + dy <= 50 and is_on_edge(rectangle, x + dx, y + dy) and visited[x+dx][y+dy] == False:
            visited[x+dx][y+dy] = True
            
            ret = min(ret, 1 + dfs(x+dx, y+dy, visited, rectangle, itemX, itemY, moves))
            
            visited[x+dx][y+dy] = False
            
    return ret

def is_on_edge(rectangle, x, y):
    n = len(rectangle)
    
    outside = 0
    on_edge = 0
    
    for i in range(len(rectangle)):
        x1, y1 = rectangle[i][0], rectangle[i][1]
        x2, y2 = rectangle[i][2], rectangle[i][1]
        x3, y3 = rectangle[i][0], rectangle[i][3]
        x4, y4 = rectangle[i][2], rectangle[i][3]
        
        if (x < x1 and x < x2 and x < x3 and x < x4) or (x > x1 and x > x2 and x > x3 and x > x4) or (y < y1 and y < y2 and y < y3 and y < y4) or (y > y1 and y > y2 and y > y3 and y > y4):
            outside += 1
            
        elif x in [x1, x2, x3, x4] or y in [y1, y2, y3, y4]:
            on_edge += 1
            
    if outside + on_edge == n and on_edge >= 1:
        return True
    else:
        return False
    
    