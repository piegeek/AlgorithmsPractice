import sys

INF = 10 ** 9
sys.setrecursionlimit(10 ** 6)

def elevatorrides():
    n, x, weights = parse_input()
    solve_elevatorrides(n, x, weights)

def solve_elevatorrides(n, x, weights):
    cache = {}
    visited = 0

    ret = INF

    for i in range(n):
        visited |= (1 << i)
        ret = min(ret, dp(visited, weights[i], n, x, weights, cache))
        visited &= ~(1 << i)

    print(ret)
    return ret

def dp(visited, current_sum, n, x, weights, cache):
    # Off by one - should return 1 here, can be shown by solving by hand
    if visited == ((1 << n) - 1):
        return 1

    if (visited, current_sum) in cache:
        return cache[(visited, current_sum)]

    ret = INF

    for i in range(n):
        if not (visited & (1 << i)):
            if current_sum + weights[i] > x:
                visited |= (1 << i)
                ret = min(ret, 1 + dp(visited, 0 + weights[i], n, x, weights, cache))
                visited &= ~(1 << i)
            else:
                visited |= (1 << i)
                ret = min(ret, dp(visited, current_sum + weights[i], n, x, weights, cache))
                visited &= ~(1 << i)

    cache[(visited, current_sum)] = ret
    return ret

def parse_input():
    input = sys.stdin.readline
    
    n, x = map(int, input().split())
    weights = list(map(int, input().split()))
    
    return n, x, weights


if __name__ == "__main__":
    elevatorrides()