from bisect import bisect_left

class Solution:
    def rowWithMax1s(self, arr):
        max_ones = 0
        ans = -1
        m = len(arr[0])

        for i in range(len(arr)):
            idx = bisect_left(arr[i], 1)
            ones = m - idx
            if ones > max_ones:
                max_ones = ones
                ans = i

        return ans
