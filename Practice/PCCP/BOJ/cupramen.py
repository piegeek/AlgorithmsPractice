import sys
import heapq

def cupramen():
    N, problems = parse_input()
    solve_cupramen(N, problems)

def solve_cupramen(N, problems):
    # Constraint: deadline
    problems = sorted(problems, key = lambda x : x[0])

    solved = []

    heap = []

    for problem in problems:
        d, v = problem
        heapq.heappush(heap, (d, (-1) * v))

    for i in range(1, N+1):
        while len(heap) > 0 and heap[0][0] < i:
            heapq.heappop(heap)

        if len(heap) > 0:
            solved.append(heapq.heappop(heap)[1] * (-1))

    ret = sum(solved)
    print(ret)
    return ret


def parse_input():
    input = sys.stdin.readline  # fast I/O
    
    N = int(input().strip())
    
    problems = []
    for _ in range(N):
        deadline, ramen = map(int, input().split())
        problems.append((deadline, ramen))
    
    return N, problems


# Example usage
if __name__ == "__main__":
    cupramen()