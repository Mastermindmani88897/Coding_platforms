class Solution:
    def largestMagicSquare(self, grid):
        m,n=len(grid),len(grid[0])
        
        rs=[[0]*(n+1) for _ in range(m+1)]
        cs=[[0]*(n+1) for _ in range(m+1)]
        d1=[[0]*(n+1) for _ in range(m+1)]
        d2=[[0]*(n+2) for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                rs[i+1][j+1]=rs[i+1][j]+grid[i][j]
                cs[i+1][j+1]=cs[i][j+1]+grid[i][j]
                d1[i+1][j+1]=d1[i][j]+grid[i][j]
                d2[i+1][j]=d2[i][j+1]+grid[i][j]
        
        def check(r,c,k):
            s=rs[r+1][c+k]-rs[r+1][c]
            if d1[r+k][c+k]-d1[r][c]!=s: return False
            if d2[r+k][c]-d2[r][c+k]!=s: return False
            for i in range(k):
                if rs[r+i+1][c+k]-rs[r+i+1][c]!=s: return False
                if cs[r+k][c+i+1]-cs[r][c+i+1]!=s: return False
            return True
        
        ans=1
        for k in range(2,min(m,n)+1):
            for i in range(m-k+1):
                for j in range(n-k+1):
                    if check(i,j,k):
                        ans=k
        return ans
