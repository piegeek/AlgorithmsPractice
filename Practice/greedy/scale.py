# BOJ 2437
import sys
import copy

def scale():
    N, weights = parse_input()
    solve_scale(N, weights)

def solve_scale(N, weights):
    subsets = []
    stack = []
    dfs(0, N, weights, stack, subsets)

    sums = sorted([sum(x) for x in subsets])
    max_sum = sums[-1]
    min_sum = sums[0]

    ret = max_sum + 1

    for t in range(min_sum, max_sum + 1):
        if t not in sums:
            ret = t
            break

    print(ret)
    return ret

def dfs(idx, N, weights, stack, subsets):
    if idx == N:
        stack_copy = copy.deepcopy(stack)
        subsets.append(stack_copy)
        return 

    # Skip
    dfs(idx + 1, N, weights, stack, subsets)

    # Take
    stack.append(weights[idx])
    dfs(idx + 1, N, weights, stack, subsets)
    stack.pop(-1)

def parse_input():
    input = sys.stdin.readline  # fast input
    
    N = int(input().strip())
    weights = list(map(int, input().split()))
    
    return N, weights


# Example usage
if __name__ == "__main__":
    scale()