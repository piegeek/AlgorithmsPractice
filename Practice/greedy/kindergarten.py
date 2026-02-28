# BOJ 13164
import sys

INF = 10 ** 9

def kindergarten():
    N, K, heights = parse_input()
    solve_kindergarten(N, K, heights)

def solve_kindergarten(N, K, heights):
    heights = sorted(heights)
    ret = dp(0, 0, 0, N, K, heights)
    print(ret)
    return ret

def dp(idx, count, last, N, K, heights):
    if count == K:
        return sum(heights[last:])

    ret = INF
    
    # Take
    ret = dp(idx + 1, count + 1, idx + 1, N, K, heights) + heights[idx] - heights[last]

    # Skip
    # Feasibility check
    if (N - 1 - idx) >= K - count:
        ret = min(ret, dp(idx + 1, count, last, N, K, heights))

    return ret

def greedy(N, K, heights):
    pass
        
def parse_input():
    input = sys.stdin.readline  # fast input
    
    N, K = map(int, input().split())
    heights = list(map(int, input().split()))
    
    return N, K, heights


# Example usage
if __name__ == "__main__":
    kindergarten()