import sys

INF = 10 ** 9

def LAN():
    test_cases = parse_input()

    for i, (N, M, xs, ys, adj_list) in enumerate(test_cases, 1):
        solve_LAN(N, M, xs, ys, adj_list)

def solve_LAN(N, M, xs, ys, adj_list):
    MSTs = []
    for node in range(N):
        visited = (1 << node)
        MST = []
        mst_dfs(node, visited, N, M, adj_list, MST)
        MST = sorted(MST)
        if MST not in MSTs:
            MSTs.append(MST)

    # print(MSTs)

    ret = INF

    visited = 0
    for i in range(len(MSTs)):
        visited |= (1 << i)
        ret = min(ret, dp(i, visited, xs, ys, MSTs, [i]))
        visited &= ~(1 << i)

    print(ret)
    return ret

def get_min_dist(last, i, xs, ys, MSTs, path):
    last_points = []

    for p in path:
        last_points += MSTs[p]

    # print(last_points)

    ith_points = MSTs[i]

    ret = INF

    for l in last_points:
        for ith in ith_points:
            distance = ((xs[l] - xs[ith]) ** 2 + (ys[l] - ys[ith]) ** 2) ** (1/2)
            # print(f'distance: {distance}')
            ret = min(ret, ((xs[l] - xs[ith]) ** 2 + (ys[l] - ys[ith]) ** 2) ** (1/2))

    return ret

def dp(last, visited, xs, ys, MSTs, path):
    if visited == (1 << len(MSTs)) - 1:
        return 0

    ret = INF

    for i in range(len(MSTs)):
        if not (visited & (1 << i)):
            visited |= (1 << i)
            path.append(i)
            ret = min(ret, get_min_dist(last, i, xs, ys, MSTs, path[:-1]) + dp(i, visited, xs, ys, MSTs, path))
            visited &= ~(1 << i)
            path.pop(-1)

    return ret

def mst_dfs(node, visited, N, M, adj_list, MST):
    MST.append(node)

    for v in adj_list[node]:
        if not (visited & (1 << v)):
            visited |= (1 << v)
            mst_dfs(v, visited, N, M, adj_list, MST)

def parse_input():
    input = sys.stdin.readline

    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        N, M = map(int, input().split())

        x_coords = list(map(int, input().split()))
        y_coords = list(map(int, input().split()))

        adj_list = [ [  ] for _ in range(N) ]
        for _ in range(M):
            a, b = map(int, input().split())
            adj_list[a].append(b)
            adj_list[b].append(a)

        test_cases.append((N, M, x_coords, y_coords, adj_list))

    return test_cases


# Example usage
if __name__ == "__main__":
    LAN()