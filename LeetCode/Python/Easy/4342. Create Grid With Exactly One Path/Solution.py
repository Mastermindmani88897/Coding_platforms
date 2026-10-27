class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#'] * n for _ in range(m)]
        
        if m == 1:
            for j in range(n):
                grid[0][j] = '.'
        elif n == 1:
            for i in range(m):
                grid[i][0] = '.'
        else:
            for j in range(n):
                grid[0][j] = '.'
            for i in range(1, m):
                grid[i][n - 1] = '.'
        
        return ["".join(row) for row in grid]