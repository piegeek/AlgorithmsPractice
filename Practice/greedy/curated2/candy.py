class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ret = [1 for _ in range(n)]

        while True:
            all_fulfilled = True

            for i in range(n-1):
                if ratings[i+1] > ratings[i] and ret[i+1] <= ret[i]:
                    all_fulfilled = False
                    ret[i+1] += 1
                elif ratings[i] > ratings[i+1] and ret[i] <= ret[i+1]:
                    all_fulfilled = False
                    ret[i] += 1
        
            if all_fulfilled:
                break

        print(ret)
        return sum(ret)

# This TLE's too...
INF = 10 ** 9

class Solution2:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ret = [INF for _ in range(n)]

        ret[0] = 1

        for i in range(1, n):
            if ratings[i] <= ratings[i-1]:
                ret[i] = 1
            else:
                ret[i] = ret[i-1] + 1

            for j in range(i, 0, -1):
                if ratings[j] < ratings[j-1] and ret[j] == ret[j-1]:
                    ret[j-1] += 1

        print(ret)
        return sum(ret)

# GPT aided solution
class Solution3:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ret = [1 for _ in range(n)]

        # Left -> Right Sweep
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                ret[i] = ret[i-1] + 1

        # Right -> Left Sweep
        for i in range(n-1, 0, -1):
            if ratings[i] < ratings[i-1]:
                ret[i-1] = max(ret[i-1], ret[i] + 1)

        print(ret)
        return sum(ret)