import sys
import heapq

# BOJ 1700
def outletscheduling():
    N, K, usage_order = parse_input()
    solve_outletscheduling(N, K, usage_order)

def solve_outletscheduling(N, K, usage_order):
    queue = []

    count = 0

    for i in range(K):
        if usage_order[i] not in [x[1] for x in queue]:
            heapq.heappush(queue, (usage_order.count(usage_order[i]), usage_order[i]))

        if len(queue) > N:
            heapq.heappop(queue)
            count += 1

    print(count)
    return count

def parse_input():
    input = sys.stdin.readline  # fast input
    
    N, K = map(int, input().split())
    usage_order = list(map(int, input().split()))
    
    return N, K, usage_order


# Example usage
if __name__ == "__main__":
    outletscheduling()