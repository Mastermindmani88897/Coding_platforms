class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        dp = [set() for _ in range(cols)]
        dp[0].add(grid[0][0])
        
        for c in range(1, cols):
            dp[c] = {x ^ grid[0][c] for x in dp[c - 1]}
            
        for r in range(1, rows):
            new_dp_0 = {x ^ grid[r][0] for x in dp[0]}
            dp[0] = new_dp_0
            for c in range(1, cols):
                prev_vals = dp[c].union(dp[c - 1])
                dp[c] = {x ^ grid[r][c] for x in prev_vals}
                
        return min(dp[cols - 1])