import sys

MOD = 10 ** 9 + 7

sys.setrecursionlimit(10 ** 6)

def twosets2():
    n = parse_input()
    solve_twosets2(n)

# Solve with bitmask traversal
def solve_twosets2(n):
    cache = {}
    visited = 0
    ret = dp(0, visited, n, cache)
    answers = reconstruct(0, visited, n, cache)

    ret = int(ret / 2) 

    print(ret)
    print(answers)
    return ret

def dp(idx, visited, n, cache):
    if idx == n:
        visited_sum = 0
        for i in range(n):
            # INCORRECT !!!
            # if (visited & (1 << i)) == 1:
            # CORRECT !!!
            if (visited & (1 << i)):
                visited_sum += (i + 1)

        if visited_sum == ((n * (n + 1)) / 2) * (1 / 2):
            return 1
        else:
            return 0

    if (idx, visited) in cache:
        return cache[(idx, visited)]

    ret = 0

    ret += dp(idx + 1, visited, n, cache)
    visited |= (1 << idx)
    ret += dp(idx + 1, visited, n, cache)
    visited &= ~(1 << idx)

    ret %= MOD

    cache[(idx, visited)] = ret
    return ret

def reconstruct(idx, visited, n, cache):
    if idx == n:
        visited_sum = 0
        for i in range(n):
            # INCORRECT !!!
            # if (visited & (1 << i)) == 1:
            # CORRECT !!!
            if (visited & (1 << i)):
                visited_sum += (i + 1)
        if visited_sum == ((n * (n + 1)) / 2) * (1 / 2):
            return [[]]
        else:
            return []

    answers = []

    if dp(idx + 1, visited, n, cache) > 0:
        suffixes = reconstruct(idx + 1, visited, n, cache)
        for suf in suffixes:
            answers.append(suf)
    if dp(idx + 1, visited | (1 << idx), n, cache) > 0:
        suffixes = reconstruct(idx + 1, visited | (1 << idx), n, cache)
        for suf in suffixes:
            answers.append([idx+1] + suf)

    return answers

def parse_input():
    input = sys.stdin.readline
    
    n = int(input().strip())
    
    return n


if __name__ == "__main__":
    twosets2()