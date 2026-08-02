class Solution:
    def count(self, n: int, m: int) -> int:
        dp = [1] * (m + 1)

        for _ in range(1, n):
            ndp = [0] * (m + 1)
            for prev in range(1, m + 1):
                for cur in range(1, m + 1):
                    if prev % cur == 0 or cur % prev == 0:
                        ndp[cur] += dp[prev]
            dp = ndp

        return sum(dp[1:])