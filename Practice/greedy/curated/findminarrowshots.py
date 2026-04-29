class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        S = []

        n = len(points)

        points = sorted(points, key = lambda x : x[1])

        for e in points:
            # cand = S + [e]

            # cand = sorted(cand, key = lambda x : (x[0], x[1]))

            # if is_independent(cand):
            #     S = cand

            start, end = e

            if len(S) == 0:
                S.append(e)

            if len(S) > 0 and start > S[-1][1]:
                S.append(e)

        return len(S)


def is_independent(cand):
    curr_end = cand[0][1]

    for i in range(1, len(cand)):
        start, end = cand[i]

        if start <= curr_end:
            return False

        curr_end = end

    return True

            
        