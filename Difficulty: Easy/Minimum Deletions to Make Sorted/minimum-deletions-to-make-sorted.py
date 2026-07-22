from bisect import bisect_left

class Solution:
    def minDeletions(self, arr):
        dp = []
        for x in arr:
            idx = bisect_left(dp, x)
            if idx == len(dp):
                dp.append(x)
            else:
                dp[idx] = x
        return len(arr) - len(dp)