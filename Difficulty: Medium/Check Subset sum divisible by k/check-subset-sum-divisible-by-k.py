class Solution:
    def divisibleByK(self, arr, k):
        dp = [False] * k

        for x in arr:
            x %= k
            ndp = dp[:]
            ndp[x] = True

            for r in range(k):
                if dp[r]:
                    ndp[(r + x) % k] = True

            dp = ndp

            if dp[0]:
                return True

        return False