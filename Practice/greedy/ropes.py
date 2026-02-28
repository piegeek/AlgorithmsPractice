# BOJ 2217
import sys

def ropes():
    N, ropes = parse_input()
    solve_ropes(N, ropes)

def solve_ropes(N, ropes):
    ropes = sorted(ropes)

    ret = N * ropes[0]
    print(ret)
    return ret

def parse_input():
    input = sys.stdin.readline  # fast input
    
    N = int(input().strip())
    
    ropes = []
    for _ in range(N):
        weight = int(input().strip())
        ropes.append(weight)
    
    return N, ropes


# Example usage
if __name__ == "__main__":
    ropes()