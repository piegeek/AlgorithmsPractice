import sys

sys.setrecursionlimit(10 ** 6)

MOD = 10 ** 9 + 7

def dicecombinations():
    n = parse_input()
    solve_dicecombinations(n)

def solve_dicecombinations(n):
    ret = 0

    cache = {}

    for i in range(1, 6+1):
        if i <= n:
            ret += dfs(i, n, cache)

    ret %= MOD

    print(ret)
    return ret

def dfs(num_sum, n, cache):
    if num_sum == n:
        return 1

    if num_sum in cache:
        return cache[num_sum]

    ret = 0

    for i in range(1, 6+1):
        if num_sum + i <= n:
            ret += dfs(num_sum + i, n, cache)

    ret %= MOD

    cache[num_sum] = ret
    return ret


def parse_input():
    input = sys.stdin.readline
    n = int(input().strip())
    return n


if __name__ == "__main__":
    dicecombinations()