# BOJ 1931
import sys

def classroomallocation():
    N, meetings = parse_input()
    solve_classroomallocation(N, meetings)

def solve_classroomallocation(N, meetings):
    # DP solution
    # visited = 0

    # ret = 1

    # for i in range(N):
    #     visited |= (1 << i)
    #     ret = max(ret, dp(visited, N, meetings, meetings[i][1]))
    #     # Backtracking
    #     visited &= ~(1 << i)

    # print(ret)
    # return ret

    # Greedy solution
    ret = greedy(N, meetings)
    print(ret)
    return ret

def dp(visited, N, meetings, last_finish_time):
    ret = 1

    for i in range(N):
        # Feasibility
        if (visited & (1 << i)) == 0 and meetings[i][0] >= last_finish_time:
            visited |= (1 << i) 
            ret = max(ret, 1 + dp(visited, N, meetings, meetings[i][1]))
            # Backtracking
            visited &= ~(1 << i)

    return ret

def greedy(N, meetings):
    meetings = sorted(meetings, key = lambda x : x[1])

    finish_time = 0

    count = 0

    for i in range(len(meetings)):
        start_time = meetings[i][0]
        if start_time >= finish_time:
            count += 1
            finish_time = meetings[i][1]

    return count

def parse_input():
    input = sys.stdin.readline  # fast input for large N (up to 100,000)
    
    N = int(input().strip())
    
    meetings = []
    for _ in range(N):
        start, end = map(int, input().split())
        meetings.append((start, end))
    
    return N, meetings


# Example usage
if __name__ == "__main__":
    classroomallocation()