class Solution:
    def maxPathScore(self, grid, k):
        m, n = len(grid), len(grid[0])
        
        dp = [[[-1]*(k+1) for _ in range(n)] for _ in range(m)]
        
        cost = 0 if grid[0][0] == 0 else 1
        score = grid[0][0]
        
        if cost <= k:
            dp[0][0][cost] = score
        
        for i in range(m):
            for j in range(n):
                for c in range(k+1):
                    if dp[i][j][c] == -1:
                        continue
                    
                    for di, dj in [(1,0),(0,1)]:
                        ni, nj = i + di, j + dj
                        
                        if ni < m and nj < n:
                            nc = c + (0 if grid[ni][nj] == 0 else 1)
                            if nc <= k:
                                ns = dp[i][j][c] + grid[ni][nj]
                                dp[ni][nj][nc] = max(dp[ni][nj][nc], ns)
        
        ans = max(dp[m-1][n-1])
        return ans if ans != -1 else -1