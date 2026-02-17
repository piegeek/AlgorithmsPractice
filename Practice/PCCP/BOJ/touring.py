import sys

sys.setrecursionlimit(10**9)

def touring():
    n, universities = parse_input()
    solve_touring(n, universities)

def solve_touring(n, universities):
    visited = [ False for _ in range(n) ]
    day = 1

    ret = dfs(visited, day, universities)

    # for i in range(len(universities)):
    #     if day <= universities[i][1]:
    #         visited[i] = True
    #         ret = max(ret, universities[i][0] + dfs(visited, day+1, universities))
    #         visited[i] = False

    print(ret)
    return ret

def dfs(visited, day, universities):
    ret = 0

    for i in range(len(visited)):
        if visited[i] == False and day <= universities[i][1]:
            visited[i] = True
            ret = max(ret, universities[i][0] + dfs(visited, day+1, universities))
            visited[i] = False

    return ret

def parse_input():
    input = sys.stdin.readline  # fast I/O
    
    n = int(input().strip())
    
    universities = []
    for _ in range(n):
        p, d = map(int, input().split())
        universities.append((p, d))
    
    return n, universities


# Example usage
if __name__ == "__main__":
    touring()