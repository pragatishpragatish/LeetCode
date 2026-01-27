class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: i[1])
        prev = intervals[0]
        count = 0

        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] >= prev[1]:
                prev = curr

            else:
                count += 1

        return count