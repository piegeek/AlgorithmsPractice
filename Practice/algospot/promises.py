import sys

INF = 10 ** 9

def promises():
    test_cases = parse_input()

    for i, (V, M, N, adj_list, future) in enumerate(test_cases, 1):
        solve_promises(V, M, N, adj_list, future)

def solve_promises(V, M, N, adj_list, future):
    ret = N

    for f in future:
        start, end, distance = f
        
        visited = (1 << start)

        # Check connectivity
        if connected_dfs(start, end, visited, V, M, N, adj_list) == False:
            ret -= 1
            adj_list[start].append([end, distance])
            adj_list[end].append([start, distance])
            continue

        # Check if reduce distance
        elif distance < distance_dfs(start, end, visited, V, M, N, adj_list):
            ret -= 1

    print(ret)
    return ret

def connected_dfs(start, end, visited, V, M, N, adj_list):
    if start == end:
        return True

    ret = False
    
    for v, d in adj_list[start]:
        if not (visited & (1 << v)):
            visited |= (1 << v)
            ret = ret or connected_dfs(v, end, visited, V, M, N, adj_list)
            visited &= ~(1 << v)

    return ret

def distance_dfs(start, end, visited, V, M, N, adj_list):
    if start == end:
        return 0

    ret = INF

    for v, d in adj_list[start]:
        if not (visited & (1 << v)):
            visited |= (1 << v)
            ret = min(ret, d + distance_dfs(v, end, visited, V, M, N, adj_list))
            visited &= ~(1 << v)

    return ret

def parse_input():
    input = sys.stdin.readline

    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        V, M, N = map(int, input().split())

        adj_list = [ [  ] for _ in range(V) ]
        for _ in range(M):
            a, b, c = map(int, input().split())
            adj_list[a].append([b, c])
            adj_list[b].append([a, c])

        future_highways = []
        for _ in range(N):
            a, b, c = map(int, input().split())
            future_highways.append((a, b, c))

        test_cases.append((V, M, N, adj_list, future_highways))

    return test_cases


# Example usage
if __name__ == "__main__":
    promises()