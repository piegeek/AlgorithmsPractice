import sys

sys.setrecursionlimit(10 ** 6)

def removalgame():
    n, arr = parse_input()
    solve_removalgame(n, arr)

def solve_removalgame(n, arr):
    cache = {}

    ret = dp(0, n-1, True, n, arr, cache)

    print(ret)
    return ret

def dp(left, right, a_turn, n, arr, cache):
    if left == right and a_turn:
        return arr[left]
    
    elif left == right and not a_turn:
        return 0

    if (left, right, a_turn) in cache:
        return cache[(left, right, a_turn)]

    if a_turn:
        # Take left
        ret = arr[left] + dp(left + 1, right, not a_turn, n, arr, cache)

        # Take right
        ret = max(ret, arr[right] + dp(left, right - 1, not a_turn, n, arr, cache))

    else:
        ret = min(dp(left + 1, right, not a_turn , n, arr, cache), dp(left, right - 1, not a_turn, n, arr, cache))

    cache[(left, right, a_turn)] = ret
    return ret

def parse_input():
    input = sys.stdin.readline
    
    n = int(input().strip())
    arr = list(map(int, input().split()))
    
    return n, arr


if __name__ == "__main__":
    removalgame()