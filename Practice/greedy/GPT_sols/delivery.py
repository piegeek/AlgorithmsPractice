import heapq

def solve_delivery(N, C, M, deliveries):
    # Sort by destination first, then start
    deliveries.sort(key=lambda x: (x[1], x[0]))

    heap = []  # min-heap by end
    current_load = 0
    delivered = 0

    for start, end, boxes in deliveries:

        # 1️⃣ Unload finished deliveries
        while heap and heap[0][0] <= start:
            finished_end, finished_boxes = heapq.heappop(heap)
            current_load -= finished_boxes
            delivered += finished_boxes

        # 2️⃣ Add current delivery within capacity
        available = C - current_load
        take = min(boxes, available)

        if take > 0:
            heapq.heappush(heap, (end, take))
            current_load += take

    # 3️⃣ Unload remaining
    while heap:
        finished_end, finished_boxes = heapq.heappop(heap)
        delivered += finished_boxes

    print(delivered)
    return delivered