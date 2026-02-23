import sys

sys.setrecursionlimit(10 ** 6)

MOD = 10 ** 9 + 7

def coincombinations1():
    n, x, coins = parse_input()
    solve_coincombinations1(n, x, coins)

# Order: o, Duplicates: o, problem asks to generate all permutations
def solve_coincombinations1(n, x, coins):
    ret = 0

    cache = {}

    for i in range(n):
        if x - coins[i] >= 0:
            ret += dfs(n, x - coins[i], coins, cache)

    ret %= MOD

    print(ret)
    return ret

def dfs(n, amount, coins, cache):
    ret = 0

    if amount == 0:
        return 1

    if amount in cache:
        return cache[amount]

    for i in range(n):
        if amount - coins[i] >= 0:
            ret += dfs(n, amount - coins[i], coins, cache)

    ret %= MOD
    cache[amount] = ret
    return ret

def parse_input():
    input = sys.stdin.readline
    
    n, x = map(int, input().split())
    coins = list(map(int, input().split()))
    
    return n, x, coins


if __name__ == "__main__": 
    coincombinations1()