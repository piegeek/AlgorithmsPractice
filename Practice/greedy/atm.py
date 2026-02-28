import sys

INF = 10 ** 9

# BOJ 11399
def atm():
    N, P = parse_input()
    solve_atm(N, P)

def solve_atm(N, P):
    P = sorted(P)

    waiting_times = [ INF for _ in range(N) ]

    for i in range(N):
        waiting_times[i] = sum(P[:i+1])

    ret = sum(waiting_times)
    print(ret)
    return ret

def parse_input():
    input = sys.stdin.readline  # fast input
    
    N = int(input().strip())
    P = list(map(int, input().split()))
    
    return N, P


# Example usage
if __name__ == "__main__":
    atm()