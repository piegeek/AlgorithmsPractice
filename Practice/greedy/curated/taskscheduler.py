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

import heapq

class Solution2:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        S = []

        # Constraint: gap of at least n intervals
        # Delay: Processes with different labels shouldn't be delayed, processes with large count shouldn't be delayed

        # Define priority: Most frequent (Most constrained, Most frequent, Earliest deadline)

        keys = set(tasks)

        count = {k: tasks.count(k) for k in keys}

        queue = []

        for key in count:
            value = count[key]
            heapq.heappush(queue, (-value, key))

        while len(queue) > 0:
            # print(queue)
            # print(S)
            num, letter = heapq.heappop(queue)

            if num == 0: continue

            num = -num

            if letter not in S[-n:]:
                S.append(letter)
                heapq.heappush(queue, (-(num - 1), letter))
            elif len([x for x in keys if x not in S[-n:]]) == 0:
                S.append('idle')
                heapq.heappush(queue, (-num, letter))
            else:
                # The problem is that when this get pushed into queue, at the next iteration, the same letter will be picked. How to avoid it?
                num2, letter2 = heapq.heappop(queue)

                num2 = -num2

                S.append(letter2)
                heapq.heappush(queue, (-(num2 - 1), letter2))
                heapq.heappush(queue, (-num, letter))

        return len(S)
            
# GPT aided solution
class Solution3:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        S = []

        # Constraint: gap of at least n intervals
        # Delay: Processes with different labels shouldn't be delayed, processes with large count shouldn't be delayed

        # Define priority: Most frequent (Most constrained, Most frequent, Earliest deadline)

        keys = set(tasks)

        count = {k: tasks.count(k) for k in keys}

        queue = []

        for key in count:
            value = count[key]
            heapq.heappush(queue, (-value, key))

        while len(queue) > 0:
            temp = []
            cycles = 0

            for _ in range(n+1):
                if len(queue) > 0:
                    num, letter = heapq.heappop(queue)
                    num = -num

                    S.append(letter)
                    cycles += 1

                    if num - 1 > 0:
                        temp.append((-(num - 1), letter))
                else:
                    break

            for item in temp:
                heapq.heappush(queue, item)

            if len(queue) > 0:
                idle_count = (n + 1) - cycles
                for _ in range(idle_count):
                    S.append('idle')

        return len(S)