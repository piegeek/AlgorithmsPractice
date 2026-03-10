import sys
import copy
import heapq

sys.setrecursionlimit(10 ** 6)

INF = 10 ** 9

def childrenday():
    test_cases = parse_input()

    for i, (D, N, M) in enumerate(test_cases, 1):
        solve_childrenday(D, N, M)

def solve_childrenday(D, N, M):
    # DFS solution diverges
    # D = sorted(D)
    # ret = INF
        
    # for digit in D:
    #     ret = min(ret, dfs(digit, D, N, M))

    # if ret == INF:
    #     print('IMPOSSIBLE')
    # else:
    #     print(ret)
    # return ret

    # BFS sol - Still TLE's for large input
    D = sorted(D)

    ret = bfs(D, N, M)
    
    if ret == INF:
        print('IMPOSSIBLE')
    else:
        print(ret)
    return ret

def bfs(D, N, M):
    queue = []

    used = []

    for digit in D:
        heapq.heappush(queue, digit)
        used.append(digit)

    while len(queue) > 0:
        curr_num = heapq.heappop(queue)

        if curr_num >= N and (curr_num - M) % N == 0:
            return curr_num

        for digit in D:
            new_num = int(str(curr_num) + str(digit))
            if new_num not in used:
                heapq.heappush(queue, new_num)
                used.append(new_num)

    return INF

def dfs(curr_num, D, N, M):
    if curr_num >= N and (curr_num - M) % N == 0:
        return curr_num

    ret = INF
    
    for digit in D:
        ret = min(ret, dfs(int(str(curr_num) + str(digit)), D, N, M))

    return ret

def parse_input():
    input = sys.stdin.readline

    T = int(input().strip())
    test_cases = []

    for _ in range(T):
        parts = input().split()
        
        # Last two numbers are N and M
        N = int(parts[-2])
        M = int(parts[-1])
        
        # The rest are digits in D
        D = list(map(int, parts[:-2]))
        
        test_cases.append((D, N, M))

    return test_cases


# Example usage
if __name__ == "__main__":
    childrenday()