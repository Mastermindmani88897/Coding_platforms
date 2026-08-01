class Solution:
    def findMax(self, n, a, b, k):
        diff = [0] * (n + 1)

        for l, r, val in zip(a, b, k):
            diff[l] += val
            if r + 1 < n:
                diff[r + 1] -= val

        ans = 0
        cur = 0
        for i in range(n):
            cur += diff[i]
            if cur > ans:
                ans = cur

        return ans