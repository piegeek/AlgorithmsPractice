import sys

def gallery():
    test_cases = parse_input()

    for i, (G, H, corridors) in enumerate(test_cases, 1):
        solve_gallery(G, H, corridors)

def solve_gallery(G, H, corridors):
    adj_mat = [ [ False for _ in range(G) ] for _ in range(G) ]
    visited = [ False for _ in range(G) ]

    for corr in corridors:
        node1, node2 = corr
        adj_mat[node1][node2] = True

    parents = [ i for i in range(G) ]
    get_roots(parents, adj_mat, G)

    roots = set(parents)

    ret = 0

    for root in roots:
        ret += dfs(root, visited, adj_mat)

    print(ret)  
    return ret

def get_roots(parents, adj_mat, G):
    visited = [False for _ in range(G)]

    for i in range(G):
        if visited[i] == False:
            find(i, i, adj_mat, parents, visited)

def find(origin, curr, adj_mat, parents, visited):
    if visited[curr] == True:
        return

    visited[curr] = True
    parents[curr] = origin

    neighbors = get_neighbors(curr, adj_mat)

    for neighbor in neighbors:
        if visited[neighbor] == False:
            find(origin, neighbor, adj_mat, parents, visited)

    # visited[curr] = False

def dfs(curr, visited, adj_mat):
    visited[curr] = True

    neighbors = get_neighbors(curr, adj_mat)

    # Leaf node
    if len(neighbors) == 0:
        return 1

    ret = 0

    for neighbor in neighbors:
        if visited[neighbor] == False:
            ret += dfs(neighbor, visited, adj_mat)

    visited[curr] = False

    return ret

def get_neighbors(curr, adj_mat):
    return [x for x in range(len(adj_mat[curr])) if adj_mat[curr][x] == True]


def parse_input():
    input = sys.stdin.readline
    
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        G, H = map(int, input().split())
        
        corridors = []
        for _ in range(H):
            a, b = map(int, input().split())
            corridors.append((a, b))
        
        test_cases.append((G, H, corridors))

    return test_cases


# Example usage
if __name__ == "__main__":
    gallery()