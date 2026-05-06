class Solution:
    def reconstructQueue(self, people):
        # Step 1: sort by height desc, k asc
        people.sort(key=lambda x: (-x[0], x[1]))

        S = []

        # Step 2: insert at index k
        for h, k in people:
            S.insert(k, [h, k])

        return S

# Simulation Based Solution
class Solution2:
    def reconstructQueue(self, people):
        people.sort(key=lambda x: (x[0], x[1]))  # small h, small k
        
        S = []
        remaining = people[:]

        while remaining:
            placed = False

            for i in range(len(remaining)):
                h, k = remaining[i]

                # check feasibility
                count = sum(1 for x in S if x[0] >= h)

                if count == k:
                    S.append([h, k])
                    remaining.pop(i)
                    placed = True
                    break

            if not placed:
                # no progress → need to reshuffle / retry
                # this is where inefficiency explodes
                raise Exception("Stuck: ordering impossible with this strategy")

        return S