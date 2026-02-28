import sys

def longestcommonsubsequence():
    n, m, a, b = parse_input()
    solve_longestcommonsubsequence(n, m, a, b)

def solve_longestcommonsubsequence(n, m, a, b):
    cache = {}

    ret = dp(0, 0, n, m, a, b, cache)

    solution = []
    reconstruct(0, 0, n, m, a, b, cache, solution)

    solutions = reconstruct_all(0, 0, n, m, a, b, cache)

    print(ret)
    # print(solution)
    print(solutions)
    return ret

def dp(i, j, n, m, a, b, cache):
    if i == n or j == m:
        return 0

    if (i, j) in cache:
        return cache[(i, j)]

    ret = 0

    for idx_a in range(i, n):
        for idx_b in range(j, m):
            if a[idx_a] == b[idx_b]:
                ret = max(ret, 1 + dp(idx_a + 1, idx_b + 1, n, m, a, b, cache))

    cache[(i, j)] = ret
    return ret

def reconstruct(i, j, n, m, a, b, cache, solution):
    if i == n or j == m:
        return

    current_val = dp(i, j, n, m, a, b, cache)

    for idx_a in range(i, n):
        for idx_b in range(j, m):
            if a[idx_a] == b[idx_b]:
                next_val = dp(idx_a + 1, idx_b + 1, n, m, a, b, cache)
                if current_val == 1 + next_val:
                    solution.append(a[idx_a])
                    reconstruct(idx_a + 1, idx_b + 1, n, m, a, b, cache, solution)
                    return

def reconstruct_all(i, j, n, m, a, b, cache):
    if i == n or j == m:
        return [[]]

    current_val = dp(i, j, n, m, a, b, cache)
    results = []

    for idx_a in range(i, n):
        for idx_b in range(j, m):
            if a[idx_a] == b[idx_b]:
                next_val = dp(idx_a + 1, idx_b + 1, n, m, a, b, cache)

                if current_val == 1 + next_val:
                    suffixes = reconstruct_all(idx_a + 1, idx_b + 1, n, m, a, b, cache)
                    for suf in suffixes:
                        results.append([a[idx_a]] + suf)

    return results
                    

def parse_input():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    return n, m, a, b


if __name__ == "__main__":
    longestcommonsubsequence()