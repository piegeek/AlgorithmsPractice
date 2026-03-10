import sys

INF = 10 ** 9

def tpath():
    test_cases = parse_input()

    for i, (N, M, adj_list) in enumerate(test_cases, 1):
        solve_tpath(N, M, adj_list)

def solve_tpath(N, M, adj_list):
    ret = INF

    visited = 0

    for v, d in adj_list[0]:
        visited |= (1 << v)
        min_speed, max_speed = dp(v, visited, N, M, adj_list)
        visited &= ~(1 << v)

        min_speed = min(min_speed, d)
        max_speed = max(max_speed, d)

        ret = min(ret, max_speed - min_speed)

    print(ret)
    return ret

def dp(last, visited, N, M, adj_list):
    if last == N - 1:
        return [INF, 0]

    min_speed = INF
    max_speed = 0

    for v, d in adj_list[last]:
        if not (visited & (1 << v)):
            visited |= (1 << v)
            min_s, max_s = dp(v, visited, N, M, adj_list)
            visited &= ~(1 << v)

            min_speed = min(min_s, d)
            max_speed = max(max_s, d)

    return [min_speed, max_speed]


def parse_input():
    input = sys.stdin.readline

    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        N, M = map(int, input().split())

        adj_list = [ [  ] for _ in range(N) ]
        for _ in range(M):
            a, b, c = map(int, input().split())
            adj_list[a].append([b, c])
            adj_list[b].append([a, c])

        test_cases.append((N, M, adj_list))

    return test_cases


# Example usage
if __name__ == "__main__":
    tpath()