import sys

INF = 10 ** 9

def routing():
    test_cases = parse_input()

    for i, (N, M, adj_mat) in enumerate(test_cases, 1):
        solve_routing(N, M, adj_mat)

def solve_routing(N, M, adj_mat):
    visited = 0

    ret = INF

    for j in range(len(adj_mat[0])):
        if adj_mat[0][j] >= 1:
            visited |= (1 << j)
            ret = min(ret, adj_mat[0][j] * dfs(j, visited, N, M, adj_mat))
            visited &= ~(1 << j)

    print(ret)
    return ret

def dfs(last, visited, N, M, adj_mat):
    if last == N - 1:
        return 1

    ret = INF

    for j in range(len(adj_mat[last])):
        if adj_mat[last][j] >= 1 and not (visited & (1 << j)):
            visited |= (1 << j)
            ret = min(ret, adj_mat[last][j] * dfs(j, visited, N, M, adj_mat))
            visited &= ~(1 << j)

    return ret

def parse_input():
    input = sys.stdin.readline

    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        N, M = map(int, input().split())

        adj_mat = [ [ 0 for _ in range(N) ] for _ in range(N) ]

        for _ in range(M):
            a, b, c = input().split()
            a = int(a)
            b = int(b)
            c = float(c)
            adj_mat[a][b] = c
            adj_mat[b][a] = c

        test_cases.append((N, M, adj_mat))

    return test_cases


# Example usage
if __name__ == "__main__":
    routing()