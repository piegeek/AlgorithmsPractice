# BOJ 8980
import sys
import heapq

def delivery():
    N, C, M, deliveries = parse_input()
    solve_delivery(N, C, M, deliveries)

def solve_delivery(N, C, M, deliveries):
    # Key - sort by (end, start)
    deliveries = sorted(deliveries, key=lambda x : (x[1], x[0]))

    queue = []

    count = 0

    for i in range(M):
        start, end, boxes = deliveries[i]

        while len(queue) > 0 and start >= queue[0][0]:
            dest, boxes_count = heapq.heappop(queue)
            count += boxes_count

        prefix_sum = sum([x[1] for x in queue])
        more_boxes_to_add = min(C - prefix_sum, boxes)
        
        if more_boxes_to_add > 0:
            heapq.heappush(queue, (end, more_boxes_to_add))

    while len(queue) > 0:
        dest, boxes_count = heapq.heappop(queue)

        count += boxes_count

    print(count)
    return count

    # DP; Exhaustive Search solution
    # ret = dp(0, C, M, deliveries, [])
    # print(ret)
    # return ret

def dp(idx, C, M, deliveries, path):
    if idx == M:
        return 0

    ret = 0
    
    path_start = [i for i in range(1, deliveries[idx][0] + 1)]
    S = sum([box_info[2] for box_info in path if box_info[1] not in path_start])
    for x in range(deliveries[idx][2]+1):
        if S + x <= C:
            path.append([deliveries[idx][0], deliveries[idx][1], x])
            ret = max(ret, x + dp(idx + 1, C, M, deliveries, path))
            path.pop(-1)

    return ret


def parse_input():
    input = sys.stdin.readline  # fast input
    
    # First line: number of villages and truck capacity
    N, C = map(int, input().split())
    
    # Second line: number of box delivery requests
    M = int(input().strip())
    
    # Next M lines: (from_village, to_village, box_count)
    deliveries = []
    for _ in range(M):
        start, end, boxes = map(int, input().split())
        deliveries.append((start, end, boxes))
    
    return N, C, M, deliveries


# Example usage
if __name__ == "__main__":
    delivery()