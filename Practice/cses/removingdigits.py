import sys

sys.setrecursionlimit(10 ** 6)
INF = 10 ** 9

def removingdigits():
    n = parse_input()
    solve_removingdigits(n)

def solve_removingdigits(n):
    str_n = str(n)
    digits = list(map(int, str_n))

    cache = {}

    ret = INF

    for i in range(len(digits)):
        if digits[i] > 0 and n - digits[i] >= 0:
            ret = min(ret, 1 + dfs(n - digits[i], cache))

    print(ret)
    return ret

def dfs(n, cache):
    # 0 steps are required to make 0 equal 0
    if n == 0:
        return 0

    if n in cache:
        return cache[n]

    ret = INF

    str_n = str(n)
    digits = list(map(int, str_n))

    for i in range(len(digits)):
        if digits[i] > 0 and n - digits[i] >= 0:
            ret = min(ret, 1 + dfs(n - digits[i], cache))

    cache[n] = ret
    return ret

def parse_input():
    input = sys.stdin.readline
    n = int(input().strip())
    return n


if __name__ == "__main__":
    removingdigits()