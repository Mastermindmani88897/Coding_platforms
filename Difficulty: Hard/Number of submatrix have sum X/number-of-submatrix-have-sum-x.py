class Solution:
    def countSquare(self, mat, x):
        n = len(mat)
        m = len(mat[0])
        
        pref = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(n):
            for j in range(m):
                pref[i+1][j+1] = (
                    mat[i][j]
                    + pref[i][j+1]
                    + pref[i+1][j]
                    - pref[i][j]
                )
        
        ans = 0
        
        for size in range(1, min(n, m) + 1):
            for i in range(n - size + 1):
                for j in range(m - size + 1):
                    total = (
                        pref[i+size][j+size]
                        - pref[i][j+size]
                        - pref[i+size][j]
                        + pref[i][j]
                    )
                    if total == x:
                        ans += 1
        
        return ans