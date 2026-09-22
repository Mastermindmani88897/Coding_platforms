class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                if max(intervals[i][0], intervals[j][0]) <= min(intervals[i][1], intervals[j][1]):
                    ans += 1

        return ans