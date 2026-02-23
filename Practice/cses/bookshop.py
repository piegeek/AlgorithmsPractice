import sys

sys.setrecursionlimit(10 ** 6)

def bookshop():
    n, x, prices, pages = parse_input()
    solve_bookshop(n, x, prices, pages)

# Order: x, Duplicates: x
def solve_bookshop(n, x, prices, pages):
    # Exploration DP
    # # visited = [ False for _ in range(n) ]
    # visited = 0

    # cache = {}
    
    # ret = dfs(n, x, prices, pages, 0, visited, cache)

    # print(ret)
    # return ret
    # Decision DP
    cache = {}

    ret = dfs_decision(n, x, prices, pages, 0, 0, cache)

    print(ret)
    return ret

# O(2 ** n * x)
def dfs(n, x, prices, pages, price_sum, visited, cache):
    if (price_sum, visited) in cache:
        return cache[(price_sum, visited)]

    ret = 0

    for i in range(n):
        # if visited[i] == False and price_sum + prices[i] <= x:
        #     visited[i] = True
        #     ret = max(ret, pages[i] + dfs(n, x, prices, pages, price_sum + prices[i], visited))
        #     # Backtracking
        #     visited[i] = False
        
        # With bitmasking
        if (visited & (1 << i)) == 0 and price_sum + prices[i] <= x:
            visited |= (1 << i)
            ret = max(ret, pages[i] + dfs(n, x, prices, pages, price_sum + prices[i], visited, cache))
            # Backtracking
            visited &= ~(1 << i)

    cache[(price_sum, visited)] = ret
    return ret

# O(n * x)
def dfs_decision(n, x, prices, pages, idx, price_sum, cache):
    if idx == n:
        return 0

    if (idx, price_sum) in cache:
        return cache[(idx, price_sum)]

    # Skip idx
    ret = dfs_decision(n, x, prices, pages, idx + 1, price_sum, cache)

    # Take idx
    if price_sum + prices[idx] <= x:
        ret = max(ret, pages[idx] + dfs_decision(n, x, prices, pages, idx + 1, price_sum + prices[idx], cache))

    cache[(idx, price_sum)] = ret
    return ret

def parse_input():
    input = sys.stdin.readline
    
    n, x = map(int, input().split())
    prices = list(map(int, input().split()))
    pages = list(map(int, input().split()))
    
    return n, x, prices, pages


if __name__ == "__main__":
    bookshop()