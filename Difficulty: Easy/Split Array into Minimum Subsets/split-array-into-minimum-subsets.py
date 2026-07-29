class Solution:
    def minSubsets(self, arr):
        arr.sort()
        ans = 1
        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1] + 1:
                ans += 1
        return ans