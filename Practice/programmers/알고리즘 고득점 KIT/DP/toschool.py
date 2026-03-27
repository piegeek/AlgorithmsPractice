import heapq

MOD = 10 ** 9 + 7
INF = 10 ** 9

def solution(m, n, puddles):
    min_distance = bfs(m, n, puddles)
    
    cache = {}
    
    ret = dp(1, 1, m, n, puddles, min_distance, 0, cache)
    
    ret %= MOD
    
    return ret
    
def dp(i, j, m, n, puddles, min_distance, curr_distance, cache):
    moves = [
        [1, 0],
        [0, 1]
    ]
    
    if (i, j) == (m, n) and curr_distance == min_distance:
        return 1
    
    if (i, j, curr_distance) in cache:
        return cache[(i, j, curr_distance)]
    
    ret = 0
    
    for move in moves:
        dx, dy = move
        if 1 <= i + dx and i + dx <= m and 1 <= j + dy and j + dy <= n and [i+dx, j+dy] not in puddles and curr_distance + 1 <= min_distance:
            ret += dp(i+dx, j+dy, m, n, puddles, min_distance, curr_distance+1, cache)
    
    ret %= MOD
    
    cache[(i, j, curr_distance)] = ret
    return ret
    
def bfs(m, n, puddles):
    moves = [
        [1, 0],
        [0, 1]
    ]
    
    origin = [1, 1]
    queue = []
    
    heapq.heappush(queue, [0, origin])
    
    while len(queue) > 0:
        step, coord = heapq.heappop(queue)
        
        x, y = coord
        
        if (x, y) == (m, n):
            return step
        
        for move in moves:
            dx, dy = move
            if 1 <= x + dx and x + dx <= m and 1 <= y + dy and y + dy <= n and [x+dx, y+dy] not in puddles:
                heapq.heappush(queue, [step+1, [x+dx, y+dy]])
        
        