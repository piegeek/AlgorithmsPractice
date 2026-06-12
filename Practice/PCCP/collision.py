def solution(points, routes):
    n = len(points)
    m = len(routes)
    
    ret = 0
    
    hist = [[] for _ in range(m)]
    
    # Initialization
    for i in range(m):
        hist[i].append(tuple(points[routes[i][0]-1]))
        
    # print(hist)
    
    # Debugging - Comment out all then Gradually remove comment
    for i in range(m):
        y, x = hist[i][0]
        route = routes[i]
        start = route[0]
        for j in range(1, len(route)):
            next = route[j]
            r = points[next-1][0] - points[start-1][0]
            c = points[next-1][1] - points[start-1][1]
            
            # Move horizontally first
            for _ in range(abs(r)):
                if r > 0:
                    hist[i].append((y+1, x))
                    y += 1
                else:
                    hist[i].append((y-1, x))
                    y -= 1
                    
            # Move vertically
            for _ in range(abs(c)):
                if c > 0:
                    hist[i].append((y, x+1))
                    x += 1
                else:
                    hist[i].append((y, x-1))
                    x -= 1
                    
            start = next
                    
    for step in range(max([len(x) for x in hist])):
        # print([x[step] for x in hist if step < len(x)])
        cand = [x[step] for x in hist if step < len(x)]
        cand_no_dup = list(set(cand))
        
        for c in cand_no_dup:
            if cand.count(c) > 1:
                ret += 1
            
    return ret
        
        
        