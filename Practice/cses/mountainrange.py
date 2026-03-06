import sys

sys.setrecursionlimit(10 ** 6)

def mountainrange():
    n, heights = parse_input()
    solve_mountainrange(n, heights)

def solve_mountainrange(n, heights):
    # ret = 1

    # for i in range(n):
    #     a = heights[i]
    #     jump = 1
    #     while i + jump < n and heights[i+jump] < heights[i]:
    #         jump += 1

    #     ret = max(ret, jump)

    cache = {}

    ret = dp(0, n-1, n, heights, cache)

    print(ret)
    return ret

def dp(left, right, n, heights, cache):
    # Leaf node
    if right <= left:
        return 1
    
    # if right - left == 1:
    #     return 1

    all_smaller = True
    for pointer in range(left+1, right+1):
        if heights[pointer] >= heights[left]:
            all_smaller = False
            break

    if all_smaller:
        # if right == n - 1:
        #     return right - left + 1
        # else:
        #     return right - left + 2
        return right - left + 1

    if (left, right) in cache:
        return cache[(left, right)]

    ret = 1

    ret = max(
        dp(left + 1, right, n, heights, cache),
        dp(left + 1, right - 1, n, heights, cache),
        dp(left, right - 1, n, heights, cache)
    )

    cache[(left, right)] = ret
    return ret

def parse_input():
    input = sys.stdin.readline
    
    n = int(input().strip())
    heights = list(map(int, input().split()))
    
    return n, heights


if __name__ == "__main__":
    mountainrange()