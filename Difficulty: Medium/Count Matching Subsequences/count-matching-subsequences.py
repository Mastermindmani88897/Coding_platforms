class Solution:
    def countWays(self, s1, s2):
        mod = 10**9 + 7
        m = len(s2)

        dp = [0] * (m + 1)
        dp[0] = 1

        for ch in s1:
            for j in range(m - 1, -1, -1):
                if ch == s2[j]:
                    dp[j + 1] = (dp[j + 1] + dp[j]) % mod

        return dp[m]