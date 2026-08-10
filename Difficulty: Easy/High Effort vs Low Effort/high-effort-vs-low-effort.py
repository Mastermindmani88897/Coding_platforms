class Solution:
    def maxTask(self, h: list[int], l: list[int]) -> int:
        n = len(h)

        dp = [0] * (n + 1)

        dp[1] = max(h[0], l[0])

        for i in range(2, n + 1):
            dp[i] = max(
                dp[i - 1] + l[i - 1],
                dp[i - 2] + h[i - 1],
                dp[i - 1]
            )

        return dp[n]