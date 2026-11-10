from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # dp[j] represents the minimum cost to reach step j (0-indexed up to n)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for j in range(1, n + 1):
            # From step i, we can jump to i + 1, i + 2, or i + 3.
            # This means to reach step j, we could have come from i = j-1, j-2, or j-3.
            for i in range(max(0, j - 3), j):
                jump_cost = costs[j - 1] + (j - i) ** 2
                dp[j] = min(dp[j], dp[i] + jump_cost)
                
        return dp[n]