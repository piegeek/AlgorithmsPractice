import sys

sys.setrecursionlimit(10 ** 6)

INF = 10 ** 9

def minimizingcoins():
    n, x, coins = parse_input()
    solve_minimizingcoins(n, x, coins)

def solve_minimizingcoins(n, x, coins):
    # Exploration DP
    # cache = {}

    # coins = sorted(coins)

    # # Off by one issue
    # ret = dfs(n, x, coins, cache) - 1

    # if ret == INF - 1:
    #     ret = -1

    # print(ret)
    # return ret

    # Decision DP
    cache = {}

    coins = sorted(coins)

    ret = dfs_decision(0, n, x, coins, cache) - 1

    if ret == INF - 1:
        ret = -1

    print(ret)
    return ret

def dfs(n, K, coins, cache):
    if K == 0:
        return 1

    if K < 0:
        return INF

    if K in cache:
        return cache[K]

    ret = INF

    for i in range(n):
        ret = min(ret, 1 + dfs(n, K - coins[i], coins, cache))
    
    cache[K] = ret
    return ret

def dfs_decision(idx, n, K, coins, cache):
    if idx == n:
        return INF

    if K == 0:
        return 1

    if K < 0:
        return INF

    if (idx, K) in cache:
        return cache[(idx, K)]

    # Skip idx
    ret = dfs_decision(idx+1, n, K, coins, cache)

    # Take idx
    if K - coins[idx] >= 0:
        ret = min(ret, 1 + dfs_decision(idx, n, K - coins[idx], coins, cache))

    cache[(idx, K)] = ret
    return ret


def parse_input():
    input = sys.stdin.readline
    
    n, x = map(int, input().split())
    coins = list(map(int, input().split()))
    
    return n, x, coins


if __name__ == "__main__":
    minimizingcoins()