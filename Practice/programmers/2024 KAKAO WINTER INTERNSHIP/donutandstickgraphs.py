def solution(edges):
    V = 1
    
    # Get vertex number
    for edge in edges:
        v1, v2 = edge
        V = max(V, v1, v2)

    adj_list = [ [] for _ in range(V + 1) ]
    
    for edge in edges:
        v1, v2 = edge
        adj_list[v1].append(v2)
        
    # print(adj_list)
    
    # Get generated
    v_in = [0 for _ in range(V+1)]
    v_out = [0 for _ in range(V+1)]
    
    for edge in edges:
        v1, v2 = edge
        v_in[v2] += 1
        v_out[v1] += 1
    
    generated = None
        
    for v in range(1, V+1):
        if v_in[v] == 0 and v_out[v] >= 2:
            generated = v
    
    ret = [generated, 0, 0, 0]
    
    for v in adj_list[generated]:
        if is_octa(v, v_in, v_out, adj_list, [v]):
            ret[3] += 1
        elif is_donut(v, v_in, v_out, adj_list):
            ret[1] += 1
        else:
            ret[2] += 1
        
    return ret

def has_cycle(v, adj_list, path):
    if v in path:
        return True
    
    ret = False
    
    for new_v in adj_list[v]:
        path.append(new_v)
        ret = ret or has_cycle(new_v, adj_list, path)
        path.pop(-1)
        
    return ret


def is_octa(v, v_in, v_out, adj_list, path):
    if v_in[v] >= 2 and v_out[v] == 2 and has_cycle(v, adj_list, [v]):
        return True
    
    ret = False
    
    for new_v in adj_list[v]:
        if new_v not in path:
            path.append(new_v)
            ret = ret or is_octa(new_v, v_in, v_out, adj_list, path)
            path.pop(-1)
        
    return ret

def is_donut(v, v_in, v_out, adj_list):
    if v_in[v] == 2 and v_out[v] == 1 and has_cycle(v, adj_list, [v]):
        return True
    return False

    
    
    
    
    