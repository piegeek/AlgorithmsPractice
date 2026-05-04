import heapq

class Solution:
    def leastInterval(self, tasks, n):
        S = []

        keys = set(tasks)
        count = {k: tasks.count(k) for k in keys}

        queue = []
        for key in count:
            heapq.heappush(queue, (-count[key], key))

        while queue:
            temp = []   # holds tasks used in this cycle
            cycle = 0   # how many slots we used in this round

            # process up to n+1 tasks
            for _ in range(n + 1):
                if queue:
                    num, letter = heapq.heappop(queue)
                    num = -num

                    S.append(letter)
                    cycle += 1

                    if num - 1 > 0:
                        temp.append((-(num - 1), letter))
                else:
                    break

            # push back remaining counts
            for item in temp:
                heapq.heappush(queue, item)

            # if heap still has work, we must fill idle
            if queue:
                idle_count = (n + 1 - cycle)
                S.extend(['idle'] * idle_count)

        return len(S)

            