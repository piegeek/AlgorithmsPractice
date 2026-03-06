import sys

MOD = 10 ** 9 + 7
sys.setrecursionlimit(10 ** 6)

def increasingsubsequence2():
    n, arr = parse_input()
    solve_increasingsubsequence2(n, arr)

def solve_increasingsubsequence2(n, arr):
    cache = {}
    ret = dp(0, -1, n, arr, cache)

    print(ret)
    return ret

def dp(idx, last, n, arr, cache):
    if idx == n:
        return 0

    if (idx, last) in cache:
        return cache[(idx, last)]

    ret = 0

    # Skip
    ret += dp(idx + 1, last, n, arr, cache)

    # Take
    if arr[idx] > last:
        ret += 1 + dp(idx + 1, arr[idx], n, arr, cache)

    ret %= MOD

    cache[(idx, last)] = ret
    return ret

def parse_input():
    input = sys.stdin.readline
    
    n = int(input().strip())
    arr = list(map(int, input().split()))
    
    return n, arr


if __name__ == "__main__":
    increasingsubsequence2()