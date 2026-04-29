import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # We're going to build up a solution
        S = []

        # The problem is asking for a permutation not a subset

        # The greedy choice seems to be spreading out the tasks as much as possible

        queue = []
        
        task_set = list(set(tasks))

        task_count = [tasks.count(task_set[i]) for i in range(len(task_set))]

        for i in range(len(task_count)):
            heapq.heappush(queue, (-task_count[i], task_set[i]))

        # print(queue)

        while len(queue) > 0:
            item = heapq.heappop(queue)
            count, task = -item[0], item[1]

            # print(item)

            if count == 0:
                continue

            possible = [x for x in task_set if x not in S[-n:]]

            if task not in possible:
                S.append('idle')
                heapq.heappush(queue, (-count, task))

            else:
                S.append(task)
                heapq.heappush(queue, (-(count - 1), task))

            # print(S)

        return len(S)
