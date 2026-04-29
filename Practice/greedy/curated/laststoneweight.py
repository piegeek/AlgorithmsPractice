import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        queue = []
        n = len(stones)
    
        for i in range(n):
            heapq.heappush(queue, -stones[i])


        while len(queue) > 0:
            stone1, stone2 = None, None
            if len(queue) > 0:
                stone1 = -heapq.heappop(queue)                
            if len(queue) > 0:
                stone2 = -heapq.heappop(queue)

            if stone2 == None:
                return stone1

            if stone1 == stone2:
                continue

            else:
                if stone1 >= stone2:
                    heapq.heappush(queue, -(stone1 - stone2))
                else:
                    heapq.heappush(queue, -(stone2 - stone1))

        return 0

        