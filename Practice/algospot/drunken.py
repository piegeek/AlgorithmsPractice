import sys

INF = 10 ** 9

def drunken():
    V, E, delays, adj_list, T, queries = parse_input()

    solve_drunken(V, E, delays, adj_list, T, queries)

def solve_drunken(V, E, delays, adj_list, T, queries):
    for query in queries:
        A, B = query
        visited = (1 << A)
        path = [[A, delays[A]]]
        ret = dfs(A, B, visited, V, E, delays, adj_list, path)

        print(ret)

def dfs(start, end, visited, V, E, delays, adj_list, path):
    if start == end:
        return max([x[1] for x in path[1:-1]])

    ret = INF

    for v, d in adj_list[start]:
        if not (visited & (1 << v)):
            visited |= (1 << v)
            path.append([v, delays[v]])
            ret = min(ret, d + dfs(v, end, visited, V, E, delays, adj_list, path))
            visited &= ~(1 << v)
            path.pop(-1)

    return ret

def parse_input():
    input = sys.stdin.readline

    # Map information
    V, E = map(int, input().split())
    delays = list(map(int, input().split()))

    adj_list = [ [  ] for _ in range(V) ]
    for _ in range(E):
        A, B, C = map(int, input().split())
        # Zero indexing
        A = A - 1
        B = B - 1
        adj_list[A].append([B, C])
        adj_list[B].append([A, C])

    # Test cases
    T = int(input().strip())
    queries = []
    for _ in range(T):
        A, B = map(int, input().split())
        # Zero indexing
        A = A - 1
        B = B - 1
        queries.append([A, B])

    return V, E, delays, adj_list, T, queries


# Example usage
if __name__ == "__main__":
    drunken()