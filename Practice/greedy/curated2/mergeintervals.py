class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        S = []

        n = len(intervals)

        intervals = sorted(intervals, key = lambda x : x[1])

        for i in range(n):
            start, end = intervals[i]

            # If it doesn't depend only on the last element, while loop + data structure
            # may work
            while len(S) > 0 and start <= S[-1][1]:
                last_start, last_end = S.pop(-1)

                start = min(start, last_start)

            S.append([start, end])

        return S
