class Solution:
    def findWays(self, grid):
        MOD = 10**9 + 7
        n = len(grid)

        ways = [[0] * n for _ in range(n)]
        best = [[-1] * n for _ in range(n)]

        ways[0][0] = 1
        best[0][0] = grid[0][0]

        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                if j > 0 and grid[i][j - 1] in (1, 3):
                    if ways[i][j - 1] > 0:
                        ways[i][j] = ways[i][j - 1]
                        best[i][j] = best[i][j - 1] + grid[i][j]

                if i > 0 and grid[i - 1][j] in (2, 3):
                    if ways[i - 1][j] > 0:
                        ways[i][j] = (ways[i][j] + ways[i - 1][j]) % MOD
                        best[i][j] = max(
                            best[i][j],
                            best[i - 1][j] + grid[i][j]
                        )

        if ways[n - 1][n - 1] == 0:
            return [0, 0]

        return [ways[n - 1][n - 1], best[n - 1][n - 1]]