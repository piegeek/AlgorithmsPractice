def solution(friends, gifts):
    N = len(friends)
    
    # create adjacency matrix
    adj_matrix = [ [ 0 for _ in range(N) ] for _ in range(N) ]
    
    for gift in gifts:
        g_from, g_to = gift.split(' ')
        from_idx = friends.index(g_from)
        to_idx = friends.index(g_to)
        
        adj_matrix[from_idx][to_idx] += 1
        
    # Create gift list
    gift_list = [ 0 for _ in range(N) ]
    
    for i in range(N):
        g_out = sum(adj_matrix[i])
        g_in = sum([ row[i] for row in adj_matrix ])
        
        gift_list[i] = g_out - g_in
        
    # print(gift_list)
    
    next_month = [ 0 for _ in range(N) ]
    
    gift_list_visited = [ [ False for _ in range(N) ] for _ in range(N) ]
    
    for i in range(N):
        for j in range(N):
            if i != j and adj_matrix[i][j] > adj_matrix[j][i]:
                next_month[i] += 1
            if i != j and adj_matrix[i][j] == adj_matrix[j][i] and gift_list_visited[i][j] == False:
                if gift_list[i] > gift_list[j]:
                    next_month[i] += 1
                elif gift_list[i] < gift_list[j]:
                    next_month[j] += 1
                    
                gift_list_visited[i][j] = True
                gift_list_visited[j][i] = True
                
    # print(next_month)
    
    return max(next_month)