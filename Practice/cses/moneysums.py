import sys

def moneysums():
    n, coins = parse_input()
    solve_moneysums(n, coins)

# Order: x, Duplicates: x
def solve_moneysums(n, coins):
    sums = []

    coins = sorted(coins)

    for k in range(1, n+1):
        generate_combinations(k, n, coins, sums)

    sums = sorted(sums)
    ret = len(sums)
    print(ret)
    print(' '.join(list(map(str, sums))))
    return ret

def generate_combinations(k, n, coins, sums):
    for i in range(n):
        dfs(k, 1, n, coins, i, sums, coins[i])

def dfs(k, level, n, coins, last, sums, path_sum):
    if level == k:
        if path_sum not in sums:
            sums.append(path_sum)
        return

    for i in range(last+1, n):
        dfs(k, level+1, n, coins, i, sums, path_sum + coins[i])
    
def parse_input():
    input = sys.stdin.readline
    
    n = int(input().strip())
    coins = list(map(int, input().split()))
    
    return n, coins

if __name__ == "__main__":
    moneysums()