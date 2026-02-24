import sys

INF = 10 ** 9

def rectanglecutting():
    a, b = parse_input()
    solve_rectanglecutting(a, b)

def solve_rectanglecutting(a, b):
    cache = {}

    ret = f(a, b, cache)
    print(ret)
    return ret

def f(a, b, cache):
    if a == b:
        return 0

    if (a, b) in cache:
        return cache[(a, b)]

    ret = INF

    if a == 1:
        for j in range(1, b):
            ret = min(ret, f(1, j, cache) + f(1, b - j, cache) + 1)

    if b == 1:
        for i in range(1, a):
            ret = min(ret, f(i, 1, cache) + f(a - i, 1, cache) + 1)

    for i in range(1, a):
        for j in range(1, b):
            ret = min(
                ret,
                f(i, b, cache) + f(a - i, b, cache) + 1,
                f(a, j, cache) + f(a, b - j, cache) + 1
            )

    cache[(a, b)] = ret
    return ret

def parse_input():
    input = sys.stdin.readline
    a, b = map(int, input().split())
    return a, b


if __name__ == "__main__":
    rectanglecutting()