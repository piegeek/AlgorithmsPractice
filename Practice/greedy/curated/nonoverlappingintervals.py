class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        S = []

        n = len(intervals)
        # intervals = sorted(intervals, key = lambda x : x[1] - x[0])
        intervals = sorted(intervals, key = lambda x : x[1])

        for e in intervals:
            cand = S + [e]

            cand = sorted(cand, key = lambda x : x[0])

            if is_independent(cand):
                S = cand

        return n - len(S)

def is_independent(cand):
    curr_end = cand[0][1]

    for i in range(1, len(cand)):
        start, end = cand[i]

        if start < curr_end:
            return False

        curr_end = end

    return True
        