class Solution:
    def countWays(self, n, m):
        mod = 10**9 + 7

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            if i < m:
                dp[i] = 1
            elif i == m:
                dp[i] = 2
            else:
                dp[i] = (dp[i - 1] + dp[i - m]) % mod

        return dp[n]