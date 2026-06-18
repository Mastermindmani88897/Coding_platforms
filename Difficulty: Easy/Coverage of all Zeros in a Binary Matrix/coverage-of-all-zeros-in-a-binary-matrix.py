class Solution:
    def findCoverage(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        left = [[False] * m for _ in range(n)]
        right = [[False] * m for _ in range(n)]
        up = [[False] * m for _ in range(n)]
        down = [[False] * m for _ in range(n)]
        
        for i in range(n):
            seen = False
            for j in range(m):
                left[i][j] = seen
                if mat[i][j] == 1:
                    seen = True
        
        for i in range(n):
            seen = False
            for j in range(m - 1, -1, -1):
                right[i][j] = seen
                if mat[i][j] == 1:
                    seen = True
        
        for j in range(m):
            seen = False
            for i in range(n):
                up[i][j] = seen
                if mat[i][j] == 1:
                    seen = True
        
        for j in range(m):
            seen = False
            for i in range(n - 1, -1, -1):
                down[i][j] = seen
                if mat[i][j] == 1:
                    seen = True
        
        ans = 0
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    ans += left[i][j]
                    ans += right[i][j]
                    ans += up[i][j]
                    ans += down[i][j]
        
        return ans