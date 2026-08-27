class Solution:
    def maxArea(self, mat: list[list[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        height = [0] * m
        ans = 0
    
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    height[j] += 1
                else:
                    height[j] = 0
    
            h = sorted(height, reverse=True)
    
            for j in range(m):
                ans = max(ans, h[j] * (j + 1))
    
        return ans