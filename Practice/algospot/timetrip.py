import sys

INF = 10 ** 9

def timetrip():
    test_cases = parse_input()

    for i, (V, W, adj_list) in enumerate(test_cases, 1):
        solve_timetrip(V, W, adj_list)

def solve_timetrip(V, W, adj_list):
    max_visited = (1 << 0)
    max_ret = max_dfs(0, 1, max_visited, V, W, adj_list, [[0, 0]])
    min_visited = (1 << 0)
    min_ret = min_dfs(0, 1, min_visited, V, W, adj_list, [[0, 0]])
    visited = (1 << 0)
    connectivity = connectivity_dfs(0, 1, visited, V, W, adj_list)

    if connectivity == False:
        print('UNREACHABLE')
        return

    if max_ret >= INF:
        max_ret = 'INFINITY'
    if min_ret <= (-1) * INF:
        min_ret = 'INFINITY'

    print(' '.join([str(min_ret), str(max_ret)]))
    return

def max_dfs(start, end, max_visited, V, W, adj_list, path):
    if start == end:
        return 0

    ret = 0

    for v, d in adj_list[start]:
        if (max_visited & (1 << v)):
            path_sum = sum([x[1] for x in path]) + d

            if path_sum > 0:
                return INF

        if not (max_visited & (1 << v)):
            max_visited |= (1 << v)
            path.append([v, d])
            ret = max(ret, d + max_dfs(v, end, max_visited, V, W, adj_list, path))
            max_visited &= ~(1 << v)
            path.pop(-1)

    return ret

def min_dfs(start, end, min_visited, V, W, adj_list, path):
    if start == end:
        return 0

    ret = INF

    for v, d in adj_list[start]:
        if (min_visited & (1 << v)):
            path_sum = sum([x[1] for x in path]) + d

            if path_sum < 0:
                return (-1) * INF

        if not (min_visited & (1 << v)):
            min_visited |= (1 << v)
            path.append([v, d])
            ret = min(ret, d + min_dfs(v, end, min_visited, V, W, adj_list, path))
            min_visited &= ~(1 << v)
            path.pop(-1)

    return ret

def connectivity_dfs(start, end, visited, V, W, adj_list):
    if start == end:
        return True

    ret = False

    for v, d in adj_list[start]:
        if not (visited & (1 << v)):
            visited |= (1 << v)
            ret = ret or connectivity_dfs(v, end, visited, V, W, adj_list)
            visited &= ~(1 << v)

    return ret

def parse_input():
    input = sys.stdin.readline

    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        V, W = map(int, input().split())

        adj_list = [ [ ] for _ in range(V) ]
        for _ in range(W):
            a, b, d = map(int, input().split())
            adj_list[a].append([b, d])

        test_cases.append((V, W, adj_list))

    return test_cases


# Example usage
if __name__ == "__main__":
    timetrip()