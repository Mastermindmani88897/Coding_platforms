class Solution:
    def diagView(self, mat):
        n = len(mat)
        res = []
        
        for d in range(2 * n - 1):
            if d < n:
                i, j = 0, d
            else:
                i, j = d - n + 1, n - 1
            
            while i < n and j >= 0:
                res.append(mat[i][j])
                i += 1
                j -= 1
        
        return res