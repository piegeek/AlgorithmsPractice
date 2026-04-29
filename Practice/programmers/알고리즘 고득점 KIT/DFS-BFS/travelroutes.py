def solution(tickets):
    begin = 'ICN'
    
    used = [False for _ in range(len(tickets))]
    
    neighbors = get_neighbors(begin, tickets, used)
    
    route = [begin]
    
    for neighbor in neighbors:
        if used[find_idx(tickets, begin, neighbor)] == False:
            used[find_idx(tickets, begin, neighbor)] = True

            dfs(neighbor, tickets, route, used)
        
    return route
        
def dfs(start, tickets, route, used):
    # print(route)
    
    neighbors = get_neighbors(start, tickets, used)
    
    route.append(start)
    
    for neighbor in neighbors:
        if used[find_idx(tickets, start, neighbor)] == False:
            used[find_idx(tickets, start, neighbor)] = True

            dfs(neighbor, tickets, route, used)
        
def get_neighbors(start, tickets, used):
    neighbors = []
    
    for i in range(len(tickets)):
        if used[i] == False and tickets[i][0] == start:
            neighbors.append(tickets[i][1])
            
    neighbors = sorted(neighbors)
    
    return neighbors

def find_idx(tickets, start, end):
    for i in range(len(tickets)):
        if tickets[i][0] == start and tickets[i][1] == end:
            return i

# New Sol

def solution(tickets):
    begin = 'ICN'
    
    used = [False for _ in range(len(tickets))]
    
    neighbors = get_neighbors(begin, tickets, used)
    
    route = [begin]
    
    for neighbor in neighbors:
        if used[find_idx(tickets, begin, neighbor)] == False:
            used[find_idx(tickets, begin, neighbor)] = True

            if dfs(neighbor, tickets, route, used):
                return route
            
            used[find_idx(tickets, begin, neighbor)] = False
        
    return route
        
def dfs(start, tickets, route, used):
    route.append(start)
    
    if len(route) == len(tickets) + 1 and all(used):
        return True
    
    neighbors = get_neighbors(start, tickets, used)
    
    for neighbor in neighbors:
        if used[find_idx(tickets, start, neighbor)] == False:
            used[find_idx(tickets, start, neighbor)] = True

            if dfs(neighbor, tickets, route, used):
                return True
            
            used[find_idx(tickets, start, neighbor)] = False
            
    route.pop(-1)
    return False
        
def get_neighbors(start, tickets, used):
    neighbors = []
    
    for i in range(len(tickets)):
        if used[i] == False and tickets[i][0] == start:
            neighbors.append(tickets[i][1])
            
    neighbors = sorted(neighbors)
    
    return neighbors

def find_idx(tickets, start, end):
    for i in range(len(tickets)):
        if tickets[i][0] == start and tickets[i][1] == end:
            return i