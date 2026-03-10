import sys
import copy
import heapq

INF = 10 ** 9

sys.setrecursionlimit(10 ** 6)

def sortgame():
    test_cases = parse_input()

    for i, (N, seq) in enumerate(test_cases, 1):
        solve_sortgame(N, seq)

def solve_sortgame(N, seq):
    # DFS
    # ret = dp(N, seq)

    # BFS
    ret = bfs(N, seq)

    print(ret)
    return ret

def bfs(N, seq):
    sorted_seq = sorted(seq)

    queue = []

    heapq.heappush(queue, [0, seq])

    while len(queue) > 0:
        step, cand = heapq.heappop(queue)

        if cand == sorted_seq:
            return step

        for i in range(0, N):
            for j in range(i, N):
                new_cand = cand[:i] + cand[i:j+1][::-1] + cand[j+1:]
                heapq.heappush(queue, [step+1, new_cand])
            

# DFS solution
def dp(N, seq):
    if seq == sorted(seq):
        return 0

    ret = INF

    seq_copy = copy.deepcopy(seq)

    for i in range(0, N):
        for j in range(i, N):
            seq = seq[:i] + seq[i:j+1][::-1] + seq[j+1:]
            ret = min(ret, 1 + dp(N, seq))
            # Backtracking
            seq = seq_copy

    return ret

def parse_input():
    input = sys.stdin.readline
    
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        N = int(input().strip())
        seq = list(map(int, input().split()))
        test_cases.append((N, seq))

    return test_cases


# Example usage
if __name__ == "__main__":
    sortgame()