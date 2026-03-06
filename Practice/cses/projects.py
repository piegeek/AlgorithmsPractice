import sys
import heapq

sys.setrecursionlimit(10 ** 6)

def projects():
    n, projects = parse_input()
    solve_projects(n, projects)

def solve_projects(n, projects):
    # DP sol
    # visited = 0
    # ret = 0
    # cache = {}
    # for i in range(n):
    #     visited |= (1 << i)
    #     ret = max(ret, projects[i][2] + dp(visited, projects[i][1], n, projects, cache))
    #     visited &= ~(1 << i)

    # print(ret)
    # return ret

    # Greedy sol
    ret = greedy(n, projects)
    print(ret)
    return ret

# O(2^n * W)
def dp(visited, last_end, n, projects, cache):
    if (visited, last_end) in cache:
        return cache[(visited, last_end)]

    ret = 0
    for i in range(n):
        if not (visited & (1 << i)) and projects[i][0] > last_end:
            visited |= (1 << i)
            ret = max(ret, projects[i][2] + dp(visited, projects[i][1], n, projects, cache))
            visited &= ~(1 << i)

    cache[(visited, last_end)] = ret
    return ret

def greedy(n, projects):
    projects = sorted(projects, key = lambda x : x[1])
    
    last_end = -1

    money = 0

    for proj in projects:
        if proj[0] > last_end:
            last_end = proj[1]
            money += proj[2]

    return money

def parse_input():
    input = sys.stdin.readline
    
    n = int(input().strip())
    projects = []
    
    for _ in range(n):
        a, b, p = map(int, input().split())
        projects.append((a, b, p))
    
    return n, projects


if __name__ == "__main__":
    projects()