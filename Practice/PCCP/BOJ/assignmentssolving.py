# Continue implementing -> Greedy method
import sys
import heapq

def assignmentssolving():
    N, assignments = parse_input()
    solve_assignmentssolving(N, assignments)

def solve_assignmentssolving(N, assignment):
    assignment = sorted(assignment, key = lambda x : x[0])

    heap = []

    for item in assignment:
        d, w = item
        
        # Correct here
        heapq.heappush(heap, (w, item))
        
        if len(heap) > d:
            heapq.heappop(heap)
        
        # Wrong here
        # heapq.heappush(heap, (w, item))

    weights = [ x[0] for x in heap ]
    ret = sum(weights)

    print(ret)
    return ret

def solve_assignmentssolving_old(N, assignments):
    queue = []

    for assignment in assignments:
        (d, w) = assignment[0], (-1) * assignment[1]
        heapq.heappush(queue, ((d, w), assignment))

    ret = 0
    day = 1

    while len(queue) > 0:
        (d, w), assignment = heapq.heappop(queue)
        if day < d:
            day = d
        if day == d:
            print(assignment[1])
            ret += assignment[1]
            day += 1
        else:
            pass
        
    print(ret)
    return ret


def parse_input():
    input = sys.stdin.readline  # fast I/O
    
    N = int(input().strip())
    
    assignments = []
    for _ in range(N):
        d, w = map(int, input().split())
        assignments.append((d, w))
    
    return N, assignments


# Example usage
if __name__ == "__main__":
    assignmentssolving()