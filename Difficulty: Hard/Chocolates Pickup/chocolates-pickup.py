class Solution:
    def maxChocolate(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        dp = [[[-1]*m for _ in range(m)] for _ in range(n)]
        
        for j1 in range(m):
            for j2 in range(m):
                if j1 == j2:
                    dp[n-1][j1][j2] = grid[n-1][j1]
                else:
                    dp[n-1][j1][j2] = grid[n-1][j1] + grid[n-1][j2]
        
        for i in range(n-2, -1, -1):
            for j1 in range(m):
                for j2 in range(m):
                    maxi = 0
                    for d1 in [-1, 0, 1]:
                        for d2 in [-1, 0, 1]:
                            nj1 = j1 + d1
                            nj2 = j2 + d2
                            
                            if 0 <= nj1 < m and 0 <= nj2 < m:
                                val = dp[i+1][nj1][nj2]
                                if j1 == j2:
                                    val += grid[i][j1]
                                else:
                                    val += grid[i][j1] + grid[i][j2]
                                maxi = max(maxi, val)
                    
                    dp[i][j1][j2] = maxi
        
        return dp[0][0][m-1]