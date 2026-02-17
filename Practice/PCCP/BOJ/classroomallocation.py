import sys

def classroomallocation():
    N, intervals = parse_input()
    solve_classroomallocation(N, intervals)

def solve_classroomallocation(N, intervals):
    # Overlapping intervals
    start = [ (x[0], +1) for x in intervals ]
    end = [ (x[1], -1) for x in intervals ]
    
    intervals = start + end
    intervals = sorted(intervals, key=lambda x : (x[0], x[1]))

    # print(intervals)

    cur_val = 0

    ret = 0

    for _, val in intervals:
        cur_val += val
        ret = max(ret, cur_val)

    print(ret)
    return ret

def parse_input():
    input = sys.stdin.readline  # fast I/O (important for N up to 200,000)
    
    N = int(input().strip())
    
    intervals = []
    for _ in range(N):
        S, T = map(int, input().split())
        intervals.append((S, T))
    
    return N, intervals


# Example usage
if __name__ == "__main__":
    classroomallocation()