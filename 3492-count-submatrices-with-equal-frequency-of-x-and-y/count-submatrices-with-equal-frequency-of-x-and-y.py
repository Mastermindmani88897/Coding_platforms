from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        cx = [[0]*n for _ in range(m)]
        cy = [[0]*n for _ in range(m)]
        
        count = 0
        
        for i in range(m):
            for j in range(n):
                cx[i][j] = (grid[i][j] == 'X')
                cy[i][j] = (grid[i][j] == 'Y')
                
                if i > 0:
                    cx[i][j] += cx[i-1][j]
                    cy[i][j] += cy[i-1][j]
                
                if j > 0:
                    cx[i][j] += cx[i][j-1]
                    cy[i][j] += cy[i][j-1]
                
                if i > 0 and j > 0:
                    cx[i][j] -= cx[i-1][j-1]
                    cy[i][j] -= cy[i-1][j-1]
                
                if cx[i][j] == cy[i][j] and cx[i][j] > 0:
                    count += 1
        
        return count