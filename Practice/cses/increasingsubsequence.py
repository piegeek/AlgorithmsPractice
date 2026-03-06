import sys

sys.setrecursionlimit(10 ** 6)

def increasingsubsequence():
    n, arr = parse_input()
    solve_increasingsubsequence(n, arr)

def solve_increasingsubsequence(n, arr):
    cache = {}
    ret = dp(0, -1, n, arr, cache)
    print(ret)
    return ret

def dp(idx, last_largest, n, arr, cache):
    if idx == n:
        return 0

    if (idx, last_largest) in cache:
        return cache[(idx, last_largest)]

    # Skip
    ret = dp(idx + 1, last_largest, n, arr, cache)

    # Take
    if arr[idx] > last_largest:
        ret = max(ret, 1 + dp(idx + 1, arr[idx], n, arr, cache))

    cache[(idx, last_largest)] = ret
    return ret

def parse_input():
    input = sys.stdin.readline
    
    n = int(input().strip())
    arr = list(map(int, input().split()))
    
    return n, arr


if __name__ == "__main__":
    increasingsubsequence()