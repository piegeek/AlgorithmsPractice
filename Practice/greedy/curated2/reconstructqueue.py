import heapq

# This was technically right, although TLE's
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        S = []

        n = len(people)

        # Permutation Greedy

        # Constraint: num of people
        # We shouldn't delay people with small height and small # of people in front

        people = sorted(people, key = lambda x : (x[0], x[1]))

        max_h = max([x[0] for x in people])
        min_h = min([x[0] for x in people])

        # S.append(people[0])

        while True:
            if len(S) == n:
                break

            for i in range(min_h, max_h+1):
                cand = [x for x in people if x[0] == i]
                cand_found = False
                for h, k in cand:
                    if len([x for x in S if x[0] >= h]) == k:
                        cand_found = True
                        S.append([h, k])
                        break
                
                if cand_found:
                    break        

        return S

        
import heapq

class Solution2:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        S = []

        n = len(people)

        # Permutation Greedy

        # Constraint: num of people
        # We shouldn't delay people with small height and small # of people in front

        people = sorted(people, key = lambda x : (x[0], x[1]))

        queue = []
        cooldown_queue = []

        for i in range(n):
            heapq.heappush(queue, ((people[i][0], people[i][1]), people[i]))

        while len(queue) > 0:
            if len(S) == n:
                break

            (h, k), person = heapq.heappop(queue)

            # Check feasibility if yes then add it to the solution
            if len([x for x in S if x[0] >= h]) == k:
                S.append([h, k])
                continue
            # If not, put it in the cooldown queue so that it doesn't get picked over and over again if we pushed it back into the queue. However this strategy is too strict. What if we need to use an item in the cooldown queue? 
            
            # The same thing gets chosen over and over again here
            else:
                # heapq.heappush(queue, ((h, k), person))
                cooldown_queue.append(((h, k), person))

            if len(cooldown_queue) == n - len(S):
                for item in cooldown_queue:
                    heapq.heappush(queue, item)   

        return S

        