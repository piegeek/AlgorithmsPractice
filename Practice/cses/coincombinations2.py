import sys

sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 9 + 7

def coincombinations2():
    n, x, coins = parse_input()
    solve_coincombinations2(n, x, coins)

# Order: x, Duplicates: o
def solve_coincombinations2(n, x, coins):
    # Exploration DP
    coins = sorted(coins)

    cache = {}

    ret = 0

    for i in range(n):
        if x - coins[i] >= 0:
            ret += dfs(n, x - coins[i], coins, i, cache)

    ret %= MOD
    print(ret)
    return ret

def dfs(n, amount, coins, last, cache):
    if amount == 0:
        return 1

    if (amount, last) in cache:
        return cache[(amount, last)]

    ret = 0

    for i in range(last, n):
        if amount - coins[i] >= 0:
            ret += dfs(n, amount - coins[i], coins, i, cache)

    ret %= MOD
    cache[(amount, last)] = ret
    return ret
    

def parse_input():
    input = sys.stdin.readline
    
    n, x = map(int, input().split())
    coins = list(map(int, input().split()))
    
    return n, x, coins


if __name__ == "__main__":
    coincombinations2()